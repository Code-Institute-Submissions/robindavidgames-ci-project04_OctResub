from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Recipe, User, RecipeTag
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    """
    Use the Generic Views to create a list of recipes.
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):
    """
    Create a view for recipe details.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Get the recipe and associated comments.
        """

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by(
            "-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        # This line and understanding of many-to-many relationships with
        # guidance from Tutor Support.
        tags = recipe.recipetag_set.all()
        print(tags)

        return render(
            request,
            "recipes/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "tags": tags
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Allow for submission of a comment.
        """

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by(
            "-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipes/recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class RecipeLike(View):
    """
    Allow the user to like a recipe.
    """

    def post(self, request, slug, *args, **kwargs):
        """
        Action when user clicks on like button.
        """
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class RecipePost(SuccessMessageMixin, CreateView):
    """
    Allow the user to create a new recipe.
    """

    model = Recipe
    fields = [
        'title',
        'slug',
        'content',
        'featured_image',
        'excerpt',
        'status',
        ]

    # This function to enable crispy forms.
    # Taken from https://stackoverflow.com/questions/23885036/how-to-use-createview-with-crispy-forms-in-django
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit(
            'submit',
            'Create',
            css_class='btn-primary'
            ))
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_message = "Post was created successfully."
    success_url = '/'


# Created with help from Tutor Support.
class EditRecipe(SuccessMessageMixin, UpdateView):
    """
    Allow the user to edit an existing recipe.
    """

    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/edit_post.html'
    success_message = "Post was edited successfully."

    # Adapted from https://stackoverflow.com/questions/11027996/success-url-in-updateview-based-on-passed-value
    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse('recipe_detail', kwargs={'slug': slug})


class RecipeDelete(SuccessMessageMixin, DeleteView):
    """
    Allow the user to delete an existing recipe.
    """

    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/delete_post.html'
    success_message = "Post was deleted successfully."
    success_url = '/'

    # This code fix taken from
    # https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(RecipeDelete, self).delete(request, *args, **kwargs)

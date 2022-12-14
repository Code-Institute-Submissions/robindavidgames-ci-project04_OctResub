from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name="recipe_likes"),
    path('newpost', views.RecipePost.as_view(), name="recipe_post"),
    path('edit/<slug:slug>', views.EditRecipe.as_view(), name="recipe_edit"),
    path(
        'delete/<slug:slug>',
        views.RecipeDelete.as_view(),
        name="recipe_delete"
        ),
]

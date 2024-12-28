from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("distributeur/", views.distributeur, name="distributeur"),
    path("invoices/", views.show_invoices, name="show_invoices"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("ajout_produit/", views.ajout_produit, name="ajout_produit"),
    path("achat_produit/", views.achat_produit, name="achat_produit"),
]

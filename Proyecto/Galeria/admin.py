
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.urls import path
from django.http import HttpResponseRedirect
from .forms import AdminLoginForm
from .models import *  # Importa todos tus modelos

class MyAdminSite(AdminSite):
    login_form = AdminLoginForm

    def login(self, request, extra_context=None):
        if request.method == "POST":
            form = self.login_form(request, data=request.POST)
            if form.is_valid():
                return HttpResponseRedirect(self.get_success_url(request))
        else:
            form = self.login_form(request)

        context = {
            **self.each_context(request),
            'form': form,
            'title': self.login_form.title,
        }
        return self.render_login_form(request, context)

admin_site = MyAdminSite()
admin_site.register(Obra)  # Reemplaza 'Obra' con tus modelos

# Registrar otros modelos según sea necesario
admin_site.register(Empleado)
admin_site.register(Contacto)

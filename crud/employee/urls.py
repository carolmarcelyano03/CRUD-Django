from django.contrib import admin  
from django.urls import path  
from employee import views  

urlpatterns = [  
    path('', views.index),
    path('admin/', admin.site.urls),  
    # URL Employee
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
    # URL Educaation
    path('ed', views.emped),
    path('showed', views.showed),
    path('edit/ed/<int:id>', views.edited),
    path('update-ed/<int:id>', views.updateed),
    path('delete/ed/<int:id>', views.destroyed),
    # URL Experience
    path('ex', views.empex),
    path('showex', views.showex),
    path('edit/ex/<int:id>', views.editex),
    path('upex/<int:id>', views.updatex),
    path('delete/ex/<int:id>', views.destroyex),
    # URL Image
    path('image', views.add_image, name="add-image"),
    path('show-image', views.show_image),
    path('delete-img/<int:id>', views.destroy_image)
]  


from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.login,name="login"),

    # Operators
    path("add_operator/",views.add_operator,name="add_operator"),
    path("get_operator/",views.get_operator,name="get_operator"),
    path("update_operator/<int:operator_id>/", views.update_operator, name="update-operator"),
    path("delete_operator/<int:operator_id>/", views.delete_operator, name="delete-operator"),
    
    # Users
    path("create_user/",views.create_user,name="create_user"),
    path("get_all_users/",views.get_all_users,name="get_all_users"),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),

    # Companies
    path("get_companies/",views.get_companies,name="get_companies"),
    path("add_company/",views.add_company,name="add_company"),
    path("bulk_upload_company/",views.bulk_upload_company,name="bulk_upload_company"),
    path('update_company/<int:pk>/', views.update_company, name='update_company'),
    path('delete_company/<int:pk>/', views.delete_company, name='delete_company'),

    # Material Type
    path("get_material_type/",views.get_material_type,name="get_material_type"),
    path("add_material_type/",views.add_material_type,name="add_material_type"),
    path('update_material_type/<int:pk>/', views.update_material_type, name="update_material_type"),
    path('delete_material_type/<int:pk>/', views.delete_material_type, name="delete_material_type"),

    # Machines
    path("get_machines/",views.get_machines,name="get_machines"),
    path("add_machine/",views.add_machine,name="add_machine"),
    path('update_machine/<int:id>/', views.update_machine, name='update_machine'),
    path('delete_machine/<int:id>/', views.delete_machine, name='delete_machine'),

    # Full Product Details
    path("add_full_product/",views.add_full_product,name="add_full_product"),
    path("get_full_products/",views.get_full_products,name="get_full_products"),

    # Programmer
    path("add_programer_Details/",views.add_programer_Details,name="add_programer_Details"),
    path("get_programer_Details/",views.get_programer_Details,name="get_programer_Details"),
    path("create_pending_material/",views.create_pending_material,name="create_pending_material"),

    # QA
    path("add_qa_details/",views.add_qa_details,name="add_qa_details"),
    path("get_qa_details/",views.get_qa_details,name="get_qa_details"),

    # Accounts
    path("add_acc_details/",views.add_acc_details,name="add_acc_details"),
    path("get_acc_details/",views.get_acc_details,name="get_acc_details"),

    # Admin
    path("get_role_list/",views.get_role_list,name="get_role_list"),
    path("total_product/",views.total_product,name="total_product"),
    path("get_overall_details/",views.get_overall_details,name="get_overall_details"),
    path("export_overall_details/",views.export_overall_details,name="export_overall_details"),
    path("export_specific_details/<str:ids>/", views.export_specific_details, name="export_specific_details"),
    
    # Admin Update
    path("update_product_details/<int:product_id>/", views.update_product_details, name="update_product_details"),
    path("update_programer_details/<int:product_id>/",views.update_programer_details,name="update_programer_details"),
    path("update_qa_details/<int:product_id>/",views.update_qa_details,name="update_qa_details"),
        
    path("filter_overall_details/",views.filter_overall_details,name="filter_overall_details"),

    path("operator_report/", views.operator_report, name="operator_report"),

    path("report/", views.universal_report, name="universal_report"),


]

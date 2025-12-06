from rest_framework import serializers
from .models import (
    product_details,
    Admin,
    product_details,
    product_material,
    company,
    programer_details,
    acc_details,
    Qa_details,
    material_type,
    All_User,
)


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class All_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = All_User
        fields = "__all__"


# Company
class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = "__all__"


# Material Type
class material_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = material_type
        fields = "__all__"


# inward
class product_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_details
        fields = "__all__"


# Material
class product_materialSerializer(serializers.ModelSerializer):
    class Meta:
        model = product_material
        fields = "__all__"


# Programer Serial
class programer_detailsSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = programer_details
        fields = "__all__"

    def get_created_by(self, obj):
        return obj.created_by.username if obj.created_by else None


# Qa
class Qa_detailsSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="product_details.id", read_only=True)
    material_id = serializers.IntegerField(source="material_details.id", read_only=True)
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Qa_details
        fields = [
            "id",
            "product_id",
            "material_id",
            "processed_date",
            "shift",
            "no_of_sheets",
            "cycletime_per_sheet",
            "total_cycle_time",
            "machines_used",
            "created_by",
        ]

    def get_material_id(self, obj):
        return obj.material_details.id if obj.material_details else None

    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.username


# Accounts Serial
class acc_detailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = acc_details
        fields = "__all__"

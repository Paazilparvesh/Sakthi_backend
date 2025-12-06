from django.db import models
from datetime import datetime
from django.db.models import JSONField


class Role(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class All_User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.ManyToManyField(Role, blank=True)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} - {self.role}"


class Admin(models.Model):
    user = models.OneToOneField(
        All_User, on_delete=models.CASCADE, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        all_role = Role.objects.all()
        self.user.isAdmin = True
        self.user.save()
        self.user.role.set(all_role)
        super.save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.id}"


# Company
class company(models.Model):
    company_name = models.CharField(max_length=30, null=True, blank=True)
    customer_name = models.CharField(max_length=30, null=True, blank=True)
    contact_no = models.CharField(max_length=15, null=True, blank=True)
    customer_dc_no = models.CharField(max_length=30, null=True, blank=True)

    def _str_(self):
        return f"{self.company_name} -{self.contact_no}--{self.id}"


# Operators
class operator_details(models.Model):
    operator_name = models.CharField(max_length=30, null=True, blank=True)

    def str(self):
        return f"{self.operator_name} -- {self.id} "


# Material Type
class material_type(models.Model):
    material_name = models.CharField(max_length=10, unique=True)
    density_value = models.FloatField()

    def __str__(self):
        return f"{self.material_name} - {self.density_value}"


# Machine
class Machine(models.Model):
    machine = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.machine} -- {self.id}"


# product Models
class product_details(models.Model):
    company_name = models.CharField(max_length=30, null=True, blank=True)
    serial_number = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    inward_slip_number = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    worker_no = models.CharField(max_length=50, null=True, blank=True)
    customer_name = models.CharField(max_length=30, null=True, blank=True)
    customer_dc_no = models.CharField(max_length=30, null=True, blank=True)
    contact_no = models.CharField(max_length=30, null=True, blank=True)
    programer_status = models.CharField(max_length=30, default="pending")
    outward_status = models.CharField(max_length=30, default="pending")
    qa_status = models.CharField(max_length=30, default="pending")
    created_by = models.ForeignKey(
        All_User, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.company_name} -{self.serial_number}--{self.id}"


class product_material(models.Model):
    product_detail = models.ForeignKey(
        product_details, on_delete=models.CASCADE, null=True, blank=True
    )
    bay = models.CharField(max_length=50,blank=True,null=True)
    mat_type = models.CharField(max_length=50, blank=True, null=True)
    mat_grade = models.CharField(max_length=50, blank=True, null=True)
    thick = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    unit_weight = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    total_weight = models.FloatField(blank=True, null=True)
    stock_due = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, default="pending")
    programer_status = models.CharField(max_length=30, default="pending")
    qa_status = models.CharField(max_length=30, default="pending")
    acc_status = models.CharField(max_length=30, default="pending")

    def __str__(self):
        return f"{self.quantity} - {self.id}"


# Programer Model
class programer_details(models.Model):
    product_details = models.ForeignKey(
        product_details, on_delete=models.CASCADE, null=True, blank=True
    )
    material_details = models.ForeignKey(
        product_material, on_delete=models.CASCADE, null=True, blank=True
    )

    program_no = models.CharField(max_length=30, null=True, blank=True)
    program_date = models.DateField(auto_now_add=False)

    processed_quantity = models.FloatField(null=True, blank=True)
    balance_quantity = models.FloatField(null=True, blank=True)

    processed_width = models.FloatField(null=True, blank=True)
    processed_length = models.FloatField(null=True, blank=True)

    used_weight = models.FloatField(null=True, blank=True)
    number_of_sheets = models.FloatField(null=True, blank=True)
    cut_length_per_sheet = models.FloatField(null=True, blank=True)
    pierce_per_sheet = models.FloatField(null=True, blank=True)
    processed_mins_per_sheet = models.FloatField(null=True, blank=True)
    total_planned_hours = models.CharField(max_length=10, null=True, blank=True)
    total_meters = models.FloatField(null=True, blank=True)
    total_piercing = models.FloatField(null=True, blank=True)
    total_used_weight = models.FloatField(null=True, blank=True)
    total_no_of_sheets = models.FloatField(null=True, blank=True)
    remarks = models.CharField(max_length=150, null=True, blank=True)
    created_by = models.ForeignKey(
        All_User, on_delete=models.CASCADE, null=True, blank=True
    )

    def str(self):
        return f"{self.program_no} -{self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.material_details:
            return

        if all(
            [
                self.balance_quantity,
                self.processed_quantity,
                self.used_weight,
                self.number_of_sheets,
                self.cut_length_per_sheet,
                self.pierce_per_sheet,
                self.processed_mins_per_sheet,
                self.total_planned_hours,
                self.total_meters,
                self.total_piercing,
                self.total_used_weight,
                self.total_no_of_sheets,
            ]
        ):
            self.material_details.programer_status = "completed"
        else:
            self.material_details.programer_status = "pending"

        self.material_details.save(update_fields=["programer_status"])


# QA Model
class Qa_details(models.Model):
    product_details = models.ForeignKey(
        product_details, on_delete=models.CASCADE, null=True, blank=True
    )
    material_details = models.ForeignKey(
        product_material, on_delete=models.CASCADE, null=True, blank=True
    )
    processed_date = models.DateField(auto_now_add=False, null=True, blank=True)
    shift = models.CharField(max_length=30, null=True, blank=True)
    no_of_sheets = models.IntegerField(null=True, blank=True)
    cycletime_per_sheet = models.FloatField(null=True, blank=True)
    total_cycle_time = models.FloatField(null=True, blank=True)
    machines_used = JSONField(null=True, blank=True)
    created_by = models.ForeignKey(
        All_User, on_delete=models.CASCADE, null=True, blank=True
    )

    def str(self):
        return f"{self.product_details} -{self.id}-- {self.processed_date} "

    def save(self, *args, **kwargs):
        # 🧩 Skip status update if no material linked
        if not self.material_details:
            super().save(*args, **kwargs)
            return

        # 🧠 Decide QA status
        is_complete = all(
            [
                self.no_of_sheets,
                self.cycletime_per_sheet,
                self.total_cycle_time,
                self.machines_used,
                self.shift,
                self.processed_date,
            ]
        )

        super().save(*args, **kwargs)

        # ✅ Update the material QA status
        material = self.material_details  # already a loaded instance
        new_status = "completed" if is_complete else "pending"

        # Update only if changed (avoids redundant saves)
        if material.qa_status != new_status:
            material.qa_status = new_status
            material.save(update_fields=["qa_status"])

        # ✅ Update parent product QA status if needed
        product = self.product_details
        if product:
            all_materials = product_material.objects.filter(product_detail=product)

            # Check if every material has qa_status == "completed"
            product_status = (
                "completed"
                if all(m.qa_status == "completed" for m in all_materials)
                else "pending"
            )

            if product.qa_status != product_status:
                product.qa_status = product_status
                product.save(update_fields=["qa_status"])


# Accounts Model
class acc_details(models.Model):
    product_details = models.ForeignKey(
        product_details, on_delete=models.CASCADE, null=True, blank=True
    )
    material_details = models.ForeignKey(
        product_material, on_delete=models.CASCADE, null=True, blank=True
    )
    invoice_no = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=30, default="pending")
    remarks = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        All_User, on_delete=models.CASCADE, null=True, blank=True
    )

    def str(self):
        return f"{self.product_details} -{self.id}-- {self.invoice_no} "

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if acc_details:
            # If processing not complete, set "processing"
            if all([self.invoice_no, self.status, self.remarks]):
                self.material_details.acc_status = "completed"
            else:
                self.material_details.acc_status = "pending"
            self.material_details.save(update_fields=["acc_status"])

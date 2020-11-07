from django.db import models
from datetime import datetime


# Create your models here.

class personal_Info(models.Model):
    citizenship_type = (
        (0, "Filipino"),
        (1, "Dual Citizenship by birth"),
        (2, "Dual Citizenship by naturalization")
    );
    sex_type = (
        (0, "Male"),
        (1, "Female")
    );
    pi_pk = models.AutoField(primary_key=True)
    sur_name = models.CharField(max_length=75)
    first_name = models.CharField(max_length=75)
    middle_name = models.CharField(max_length=75, null=True, blank=True)
    name_ext = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField()
    pace_of_birth = models.CharField(max_length=100)
    sex = models.CharField(choices=sex_type, max_length=10)
    civil_status = models.CharField(max_length=15)
    height = models.IntegerField()
    weight = models.IntegerField()
    blood_type = models.CharField(max_length=5)
    gsis_id_no = models.IntegerField()
    pagibig_id_no = models.IntegerField()
    philhealth_no = models.IntegerField()
    sss_no = models.IntegerField()
    tin_no = models.IntegerField()
    agency_employee_no = models.IntegerField()
    citizenship = models.IntegerField(choices=citizenship_type)
    country = models.CharField(max_length=50, null=True, blank=True)
    res_lot_no = models.CharField(max_length=20)
    res_street = models.CharField(max_length=75)
    res_subd = models.CharField(max_length=50)
    res_brgy = models.CharField(max_length=50)
    res_city = models.CharField(max_length=50)
    res_province = models.CharField(max_length=50)
    res_zipcode = models.IntegerField()
    per_lot_no = models.CharField(max_length=20)
    per_street = models.CharField(max_length=75)
    per_subd = models.CharField(max_length=50)
    per_brgy = models.CharField(max_length=50)
    per_city = models.CharField(max_length=50)
    per_province = models.CharField(max_length=50)
    per_zipcode = models.IntegerField()
    telephone = models.IntegerField()
    mobile_no = models.IntegerField()
    email_address = models.CharField(max_length=75)
    photo = models.CharField(max_length=100)
    date_accomplished = models.DateField()
    pass


class family_Background(models.Model):
    fb_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE)
    fb_pk = models.AutoField(primary_key=True)
    spouse_sur_name = models.CharField(max_length=75, null=True, blank=True)
    spouse_first_name = models.CharField(max_length=75, null=True, blank=True)
    spouse_middle_name = models.CharField(max_length=75, null=True, blank=True)
    spouse_name_ext = models.CharField(max_length=20, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    business_name = models.CharField(max_length=150, null=True, blank=True)
    business_address = models.CharField(max_length=200, null=True, blank=True)
    spouse_telephone = models.IntegerField(null=True, blank=True)
    father_sur_name = models.CharField(max_length=75)
    father_first_name = models.CharField(max_length=75)
    father_middle_name = models.CharField(max_length=75, null=True, blank=True)
    father_name_ext = models.CharField(max_length=20, null=True, blank=True)
    mother_sur_name = models.CharField(max_length=75)
    mother_first_name = models.CharField(max_length=75)
    mother_middle_name = models.CharField(max_length=75, null=True, blank=True)
    pass


class children_Names(models.Model):
    cn_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE, default=None)
    cn_pk = models.AutoField(primary_key=True)
    child_full_name = models.CharField(max_length=150, null=True, blank=True)
    child_date_of_birth = models.DateField(null=True, blank=True)
    pass


class educational_Background(models.Model):
    levels = (
        (0, "Elementary"),
        (1, "Secondary"),
        (2, "Vocational/Trade Course"),
        (3, "College"),
        (4, "Graduate Studies"),
    );
    eb_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE)
    eb_pk = models.AutoField(primary_key=True)
    educ_level = models.CharField(choices=levels, max_length=40, null=True, blank=True)
    name_of_school = models.CharField(max_length=150, null=True, blank=True)
    degree = models.CharField(max_length=150, null=True, blank=True)
    period_from = models.DateField(null=True, blank=True)
    period_to = models.DateField(null=True, blank=True)
    highest_level_earned = models.CharField(max_length=100, null=True, blank=True)
    year_grad = models.IntegerField(null=True, blank=True)
    honors = models.CharField(max_length=50, null=True, blank=True)
    pass


class cs_Eligibility(models.Model):
    select_eligibility = (
        (0, "Career Service"),
        (1, "RA 1080 (Board/Bar) Under Special Law"),
        (2, "CES"),
        (3, "CSEE Barangay Eligibility"),
        (4, "Driver's License"),
    );
    cse_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE)
    cse_pk = models.AutoField(primary_key=True)
    eligibility = models.CharField(max_length=40, null=True, blank=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    date_of_exam = models.DateField(null=True, blank=True)
    place_of_exam = models.CharField(max_length=200, null=True, blank=True)
    license_number = models.IntegerField(null=True, blank=True)
    license_date_of_validity = models.DateField(null=True, blank=True)
    pass


class work_Experience(models.Model):
    we_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE)
    we_pk = models.AutoField(primary_key=True)
    inclusive_dates_from = models.DateField(null=True, blank=True)
    inclusive_dates_to = models.DateField(null=True, blank=True)
    position_title = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=75, null=True, blank=True)
    monthly_salary = models.IntegerField(null=True, blank=True)
    pay_grade = models.IntegerField(null=True, blank=True)
    status_of_appointment = models.CharField(max_length=50, null=True, blank=True)
    govt_service = models.BooleanField(default=False, null=True, blank=True)
    pass


class voluntary_Work(models.Model):
    vw_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE)
    vw_pk = models.AutoField(primary_key=True)
    name_add_org = models.CharField(max_length=300, null=True, blank=True)
    inclusive_date_from = models.DateField(null=True, blank=True)
    inclusive_date_to = models.DateField(null=True, blank=True)
    number_of_hours = models.IntegerField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    pass


class training_Attended(models.Model):
    ta_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE)
    ta_pk = models.AutoField(primary_key=True)
    title_of_training = models.CharField(max_length=100, null=True, blank=True)
    inclusive_date_from = models.DateField(null=True, blank=True)
    inclusive_date_to = models.DateField(null=True, blank=True)
    number_of_hours = models.IntegerField(null=True, blank=True)
    type_of_LD = models.CharField(max_length=75, null=True, blank=True)
    conducted_by = models.CharField(max_length=150, null=True, blank=True)
    pass


class other_Info(models.Model):
    oi_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE)
    oi_pk = models.AutoField(primary_key=True)
    special_skills = models.CharField(max_length=75, null=True, blank=True)
    non_acad_recognition = models.CharField(max_length=100, null=True, blank=True)
    membership = models.CharField(max_length=100, null=True, blank=True)
    pass

# class Questions(models.Model):
#     q_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE)
#     q_pk = models.AutoField(primary_key=True)
#     third_degree_question = models.BooleanField(default=False)
#     third_degree_question = models.TextField(null=True, blank=True)
#     pass


class References(models.Model):
    ref_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE)
    ref_pk = models.AutoField(primary_key=True)
    ref_name = models.CharField(max_length=150)
    ref_address = models.CharField(max_length=200)
    ref_telephone = models.IntegerField()
    pass


class issued_Govt(models.Model):
    ig_fk = models.ForeignKey(personal_Info, on_delete=models.CASCADE)
    ig_pk = models.AutoField(primary_key=True)
    id_name = models.CharField(max_length=100)
    id_no = models.IntegerField()
    date_place_of_issuance = models.CharField(max_length=100)
    pass
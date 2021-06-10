from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import  View
from hr_management_app.models import CustomUser, Staffs, Office, Branch, Department, Designation, Shift


def admin_home(request):
        return render(request, "admin_template/index.html")

class add_staff(View):
    def get(self, request):
        office=Office.objects.all()
        branch=Branch.objects.all()
        department=Department.objects.all()
        shift=Shift.objects.all()
        designation=Designation.objects.all()
        context = {
            "office": office,
            "branch": branch,
            "department": department,
            "shift": shift,
            "designation": designation
        }
        return render(request, "admin_template/add_staff.html", context)
    def post(self, request):
        if request.method != "POST":
            messages.error(request, "Invalid Method ")
        else:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            address = request.POST.get('address')
            phone = request.POST.get('phone')
            image = "image"
            office_id=request.POST.get("office")
            office=Office.objects.get(id=office_id)
            # branch = request.POST.get('branch')
            # department = request.POST.get('department')
            # shift = request.POST.get('shift')
            # designation = request.POST.get('designation')
            # duty_type = request.POST.get('duty_type')
            # card_no = request.POST.get('card_no')
            # gender = request.POST.get('gender')
            # marital_status = request.POST.get('marital_status')
            # date_of_birth = request.POST.get('date_of_birth')
            # sallery = request.POST.get('sallery')
            # sallery_type = request.POST.get('sallery_type')
            # date_of_joining = request.POST.get('date_of_join')
            # emergency_contact = request.POST.get('contact_person')
            # cityzenshipno = request.POST.get('citizenship_no')
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address=address
            user.staffs.phone=phone
            user.staffs.image=image
            # user.staffs.office_id=office
            # user.staffs.branch=branch
            # user.staffs.department=department
            # user.staffs.shift=shift
            # user.staffs.designation=designation
            # user.staffs.duty_type=duty_type
            # user.staffs.card_no=card_no
            # user.staffs.gender=gender
            # user.staffs.marital_status=marital_status
            # user.staffs.date_of_birth=date_of_birth
            # user.staffs.sallery=sallery
            # user.staffs.sallery_type=sallery_type
            # user.staffs.date_of_joining=date_of_joining
            # user.staffs.emergency_contact=emergency_contact
            # user.staffs.cityzenshipno=cityzenshipno
            user.save()
            messages.success(request, "Staff Added Successfully!")
            return render(request, 'admin_template/add_staff.html')

        except:
            messages.error(request, "Failed to Add Staff!")
            return render(request, 'admin_template/add_staff.html')
            # return redirect('add_staff')
def manage_staff(request):
    staffs = Staffs.objects.all()
    context = {
        "staffs": staffs
    }
    return render(request, "admin_template/manage_staff.html", context)

class edit_staff(View):
    def get(self, request, staff_id):
        staff = Staffs.objects.get(admin=staff_id)
        context = {"staff": staff,"id": staff_id}
        return render(request, "admin_template/edit_staff.html", context)
    def post(self, request, staff_id):
        if request.method != "POST":
             return HttpResponse("<h2>Method Not Allowed</h2>")
        else:
            staff_id = request.POST.get('staff_id')
            username = request.POST.get('username')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            address = request.POST.get('address')
        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()

             # INSERTING into Staff Model
            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Staff Updated Successfully.")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
            
        except:
            messages.error(request, "Failed to Update Staff.")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))

def delete_staff(request, staff_id):
    url = request.META.get('HTTP_REFERER')
    staff = CustomUser.objects.filter(id=staff_id)
    staff.delete()
    messages.warning(request, 'Your product has been deleted.')
    return HttpResponseRedirect(url)

# manage ofice ===================================================================
class add_office(View):
    def get(self, request):
        return render(request, "admin_template/add_office.html")
    def post(self, request):
        if request.method != "POST":
            messages.error(request, "Invalid Method ")
        else:
            name = request.POST.get('office_name')
            description = request.POST.get('description')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            registrationNo = request.POST.get('registrationNo')
            image = "image"
        try:
            office = Office(name=name, description=description, address=address, phone=phone, email=email, registrationNo=registrationNo, image=image)
            office.save()
            messages.success(request, "Staff Added Successfully!")
            return render(request, 'admin_template/add_office.html')

        except:
            messages.error(request, "Failed to Add Staff!")
            return render(request, 'admin_template/add_office.html')
            # return redirect('add_staff')

def manage_office(request):
    office = Office.objects.all()
    print(office)
    context = {
        "office": office
    }
    return render(request, "admin_template/manage_office.html", context)

class edit_office(View):
    def get(self, request, office_id):
        office = Office.objects.get(id=office_id)
        context = {"office": office,"office_id": office_id}
        return render(request, "admin_template/edit_office.html", context)
    def post(self, request, office_id):
        if request.method != "POST":
             return HttpResponse("<h2>Method Not Allowed</h2>")
        else:
            name = request.POST.get('office_name')
            description = request.POST.get('description')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            registrationNo = request.POST.get('registrationNo')
            image = "image"
        try:
           
            # INSERTING into office Model
            office = Office.objects.get(id=office_id)
            office.name = name
            office.description = description
            office.address = address
            office.phone = phone
            office.email = email
            office.registrationNo = registrationNo
            office.image = image
            
            office.save()
            messages.success(request, "Staff Updated Successfully.")
            return HttpResponseRedirect(reverse("edit_office",kwargs={"office_id":office_id}))
            
        except:
            messages.error(request, "Failed to Update Staff.")
            return HttpResponseRedirect(reverse("edit_office",kwargs={"office_id":office_id}))

def delete_office(request, office_id):
    url = request.META.get('HTTP_REFERER')
    office = Office.objects.filter(id=office_id)
    office.delete()
    messages.warning(request, 'Your product has been deleted.')
    return HttpResponseRedirect(url)
# manage branch ===================================================================
def manage_branch(request):
    branch = Branch.objects.all()
    context = {
        "branch": branch
    }
    return render(request, "admin_template/manage_branch.html", context)
class add_branch(View):
    def get(self, request):
        office=Office.objects.all()
        context = {
            "office": office
        }
        return render(request, "admin_template/add_branch.html", context)
    def post(self, request):
        if request.method != "POST":
            messages.error(request, "Invalid Method ")
        else:
            office_id = request.POST.get('company_name')
            office=Office.objects.get(id=office_id)
            branchName = request.POST.get('branch_name')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            email = request.POST.get('email')
            registrationNo = request.POST.get('registrationNo')
        try:
            branch = Branch(office_id=office, branchName=branchName, address=address, phone=phone, email=email)
            branch.save()
            messages.success(request, "Staff Added Successfully!")
            return render(request, 'admin_template/add_branch.html')

        except:
            messages.error(request, "Failed to Add Staff!")
            return render(request, 'admin_template/add_branch.html')

def delete_branch(request, branch_id):
    url = request.META.get('HTTP_REFERER')
    branch = Branch.objects.filter(id=branch_id)
    branch.delete()
    messages.warning(request, 'Your product has been deleted.')
    return HttpResponseRedirect(url)

class edit_branch(View):
    def get(self, request, branch_id):
        branch = Branch.objects.get(id=branch_id)
        context = {"branch": branch,"branch_id": branch_id}
        return render(request, "admin_template/edit_branch.html", context)
    def post(self, request, office_id):
          return render(request, "admin_template/edit_branch.html")

# manage department ===================================================================
def manage_department(request):
    department = Department.objects.all()
    context = {
        "department": department
    }
    return render(request, "admin_template/manage_department.html", context)

def delete_department(request, department_id):
    url = request.META.get('HTTP_REFERER')
    department = Department.objects.filter(id=department_id)
    department.delete()
    messages.warning(request, 'Your product has been deleted.')
    return HttpResponseRedirect(url)
class add_department(View):
    def get(self, request):
        return render(request, "admin_template/add_department.html")
    def post(self, request):
        if request.method != "POST":
            messages.error(request, "Invalid Method ")
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
        try:
            department = Department(name=name, email=email)
            department.save()
            messages.success(request, "Staff Added Successfully!")
            return render(request, 'admin_template/add_department.html')

        except:
            messages.error(request, "Failed to Add Staff!")
            return render(request, 'admin_template/add_department.html')
class edit_department(View):
    def get(self, request, department_id):
        department = Department.objects.get(id=department_id)
        context = {"department": department,"department_id": department_id}
        return render(request, "admin_template/edit_department.html", context)
    def post(self, request, office_id):
          return render(request, "admin_template/edit_department.html")

# manage designation ===================================================================
def manage_designation(request):
    designation = Designation.objects.all()
    context = {
        "designation": designation
    }
    return render(request, "admin_template/manage_designation.html", context)

class add_designation(View):
    def get(self, request):
        return render(request, "admin_template/add_designation.html")
    def post(self, request):
        if request.method != "POST":
            messages.error(request, "Invalid Method ")
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
        try:
            department = Department(name=name, email=email)
            department.save()
            messages.success(request, "Staff Added Successfully!")
            return render(request, 'admin_template/add_designation.html')

        except:
            messages.error(request, "Failed to Add Staff!")
            return render(request, 'admin_template/add_designation.html')
class edit_designation(View):
    def get(self, request, designation_id):
        designation = Designation.objects.get(id=designation_id)
        context = {"designation": designation,"designation_id": designation_id}
        return render(request, "admin_template/edit_designation.html", context)
    def post(self, request, office_id):
          return render(request, "admin_template/edit_designation.html")

def delete_designation(request, designation_id):
    url = request.META.get('HTTP_REFERER')
    designation = Designation.objects.filter(id=designation_id)
    designation.delete()
    messages.warning(request, 'Your product has been deleted.')
    return HttpResponseRedirect(url)

# manage shift ===================================================================
def manage_shift(request):
    shift = Shift.objects.all()
    context = {
        "shift": shift
    }
    return render(request, "admin_template/manage_shift.html", context)

def delete_shift(request, shift_id):
    url = request.META.get('HTTP_REFERER')
    shift = Shift.objects.filter(id=shift_id)
    shift.delete()
    messages.warning(request, 'Your product has been deleted.')
    return HttpResponseRedirect(url)

class add_shift(View):
    def get(self, request):
        return render(request, "admin_template/add_shift.html")
    def post(self, request):
        if request.method != "POST":
            messages.error(request, "Invalid Method ")
        else:
            name = request.POST.get('name')
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')
            duration = request.POST.get('shift_hour')
        try:
            print(name)
            print(start_time)
            print(end_time)
            print(duration)
            shift = Shift(name=name, start_time=start_time, end_time=end_time, duration=duration)
            shift.save()
            messages.success(request, "Staff Added Successfully!")
            return render(request, 'admin_template/add_shift.html')

        except:
            messages.error(request, "Failed to Add Staff!")
            return render(request, 'admin_template/add_shift.html')

class edit_shift(View):
    def get(self, request, shift_id):
        shift = Shift.objects.get(id=shift_id)
        context = {"shift": shift,"shift_id": shift_id}
        return render(request, "admin_template/edit_shift.html", context)
    def post(self, request, office_id):
          return render(request, "admin_template/edit_shift.html")
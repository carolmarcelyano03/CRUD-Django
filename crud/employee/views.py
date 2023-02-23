from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm
from employee.forms import EducationForm
from employee.forms import ExperienceForm
from employee.forms import PictureForm
from employee.models import Employee  
from employee.models import Education
from employee.models import Experience
from employee.models import Picture

# View Employee
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")

# View Education
def emped(request):  
    if request.method == "POST":  
        form = EducationForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/showed')  
            except:  
                pass  
    else:  
        form = EducationForm()  
    return render(request,'education.html',{'form':form}) 
def showed(request):  
    educations = Education.objects.all()  
    return render(request,"showed.html",{'educations':educations})
def edited(request, id):  
    education = Education.objects.get(id=id)  
    return render(request,'edited.html', {'education':education}) 
def updateed(request, id):  
    education = Education.objects.get(id=id)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect("/showed")
        else:
            print(form.errors)
    else:
        form = EducationForm(instance=education)
    return render(request, 'edited.html', {'education': education, 'form': form})
def destroyed(request, id):  
    education = Education.objects.get(id=id)  
    education.delete()  
    return redirect("/showed")     

# View Experience
def empex(request):  
    if request.method == "POST":  
        formEx = ExperienceForm(request.POST)  
        if formEx.is_valid():  
            try:  
                formEx.save()  
                return redirect('/showex')  
            except:  
                pass  
    else:  
        formEx = ExperienceForm()  
    return render(request,'experience.html',{'formEx':formEx}) 
def showex(request):  
    experiences = Experience.objects.all()  
    return render(request,"showex.html",{'experiences':experiences})
def editex(request, id):  
    experience = Experience.objects.get(id=id)  
    return render(request,'editex.html', {'experience':experience}) 
def updatex(request, id):  
    experience = Experience.objects.get(id=id)  
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect("/showex")
        else:
            # Tampilkan pesan error jika form tidak valid
            print(form.errors)
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'editex.html', {'experience': experience, 'form': form}) 
def destroyex(request, id):  
    experience = Experience.objects.get(id=id)  
    experience.delete()  
    return redirect("/showex")  

# View Images
def add_image(request):
    if request.method == 'POST':  
        form = PictureForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            return redirect('/show-image') 
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'add_image.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = PictureForm()  
  
    return render(request, 'add_image.html', {'form': form})

def show_image(request) :
    pictures = Picture.objects.all()  
    return render(request,"show_image.html",{'pictures':pictures})

def destroy_image(request, id):  
    picture = Picture.objects.get(id=id)  
    picture.delete()  
    return redirect("/show-image") 

def index(request):
    return redirect("/show")
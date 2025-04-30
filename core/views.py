from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher, Student, Assignment
from .forms import StudentForm, AssignmentForm

def teacher_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id_number = request.POST.get('id_number')
        try:
            teacher = Teacher.objects.get(name=name, id_number=id_number)
            request.session['teacher_id'] = teacher.id
            return redirect('home')
        except Teacher.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def teacher_logout(request):
    request.session.flush()
    return redirect('login')

def home(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login')

    teacher = Teacher.objects.get(id=teacher_id)
    students = teacher.student_set.all()

    return render(request, 'home.html', {'teacher': teacher, 'students': students})

def add_student(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login')

    teacher = Teacher.objects.get(id=teacher_id)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.teacher = teacher
            student.save()
            return redirect('home')
    else:
        form = StudentForm()
    
    return render(request, 'add_student.html', {'form': form})

def edit_student(request, student_id):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login')

    student = get_object_or_404(Student, id=student_id, teacher_id=teacher_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, student_id):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login')

    student = get_object_or_404(Student, id=student_id, teacher_id=teacher_id)

    if request.method == 'POST':
        student.delete()
        return redirect('home')

    return render(request, 'delete_student.html', {'student': student})

def add_assignment(request, student_id):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login')

    student = get_object_or_404(Student, id=student_id, teacher_id=teacher_id)

    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.student = student
            assignment.save()
            return redirect('home')
    else:
        form = AssignmentForm()

    return render(request, 'add_assignment.html', {'form': form, 'student': student})


def edit_assignment(request, assignment_id):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login')

    assignment = get_object_or_404(Assignment, id=assignment_id, student__teacher_id=teacher_id)

    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AssignmentForm(instance=assignment)

    return render(request, 'edit_assignment.html', {'form': form, 'assignment': assignment})


def delete_assignment(request, assignment_id):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('login')

    assignment = get_object_or_404(Assignment, id=assignment_id, student__teacher_id=teacher_id)
    assignment.delete()
    return redirect('home')

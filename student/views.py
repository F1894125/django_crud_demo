from django.shortcuts import render
from django.contrib import messages

student_details: dict = {}
student_list: list = []
roll_no_set: set = set()

def home(request):
    return render(request, 'student/home.html')

def add_student(request):
    global student_list, roll_no_set

    if request.method == 'POST':
        if all(request.POST.values()):
            roll_no = request.POST.get('roll_no')
            if roll_no in roll_no_set:
                messages.error(request, f"Student with roll no. '{roll_no}' already exists.")
                return render(request, 'student/add_student.html')

            roll_no_set.add(roll_no)
            student = {
                'roll_no': roll_no,
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'major': request.POST.get('major'),
                'subjects': [
                    request.POST.get('subject_1'),
                    request.POST.get('subject_2'),
                    request.POST.get('subject_3'),
                ]
            }
            student_list.append(student)
            messages.success(request, f"Student '{roll_no}' added.")
            return render(request, 'student/add_student.html')
        
        else:
            messages.error(request, "Please fill all the fields.")
            return render(request, 'student/add_student.html')
    
    return render(request, 'student/add_student.html')

def view_student(request):
    global student_list
    return render(request, 'student/view_student.html', {'students': student_list})


def edit_student(request):
    context = {}
    global student_list, roll_no_set

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'find_student':
            roll_no = request.POST.get('roll_no')
            if not roll_no:
                messages.error(request, "Please provide the roll no.")
                return render(request, 'student/edit_student.html')
        
            if roll_no in roll_no_set:
                context['student_exists'] = True
                context['roll_no'] = roll_no
                messages.success(request, f"Student with roll no. '{roll_no}' found. You can now edit the details.")
                return render(request, 'student/edit_student.html', context)
            else:
                messages.error(request, f"Student with roll no. '{roll_no}' not found.")
                return render(request, 'student/edit_student.html')
        
        elif form_type == 'update_student':
            if not all(request.POST.values()):
                context['student_exists'] = True
                messages.error(request, "Please fill all the fields.")
                return render(request, 'student/edit_student.html', context)
            
            roll_no = request.POST.get('old_roll_no')
            target_student = next(student for student in student_list if student['roll_no'] == roll_no)
            target_student['roll_no'] = request.POST.get('new_roll_no')
            target_student['first_name'] = request.POST.get('new_first_name')
            target_student['last_name'] = request.POST.get('new_last_name')
            target_student['major'] = request.POST.get('new_major')
            target_student['subjects'] = [
                request.POST.get('new_subject_1'),
                request.POST.get('new_subject_2'),
                request.POST.get('new_subject_3'),
            ]
            roll_no_set.remove(roll_no)
            roll_no_set.add(request.POST.get('new_roll_no'))
            messages.success(request, f"Student '{roll_no}' updated.")
            return render(request, 'student/edit_student.html')
    
    return render(request, 'student/edit_student.html')


def delete_student(request):
    context = {}
    global student_list, roll_no_set

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'delete_target_student':
            roll_no = request.POST.get('roll_no')
            if not roll_no:
                messages.error(request, "Please provide the roll no.")
                return render(request, 'student/delete_student.html')
            
            if roll_no in roll_no_set:
                context['student_exists'] = True
                context['roll_no'] = roll_no
                messages.success(request, f"Student with roll no. '{roll_no}' found. Please confirm deletion.")
                return render(request, 'student/delete_student.html', context)
            
            else:
                messages.error(request, f"Student with roll no. '{roll_no}' not found.")
                return render(request, 'student/delete_student.html')
        
        elif form_type == 'confirm_delete_student':
            roll_no = request.POST.get('target_roll_no')
            target_student = next(idx for idx, student in enumerate(student_list) if student['roll_no'] == roll_no)
            student_list.pop(target_student)
            roll_no_set.remove(roll_no)
            messages.success(request, f"Student '{roll_no}' deleted.")
            return render(request, 'student/delete_student.html')
    
    return render(request, 'student/delete_student.html')
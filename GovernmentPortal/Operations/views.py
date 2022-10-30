from django.shortcuts import render
from . models import Project, PublicSector, PublicComment, CabinetMember
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def homepage(request):
    project_list = Project.objects.all()
    
    for project in project_list:
        project_comment_list = PublicComment.objects.all().filter(project=project)

    
    user = request.user
    
    user_list = User.objects.all()
    number_of_users = user_list.count()
    staff_members = []
    gov_officials = CabinetMember.objects.all()
    for this_user in user_list:
        if this_user.is_staff:
            staff_members.append(this_user)

    
    context = {
        'user': user,
        'number_of_users': number_of_users,
        'staff_members': len(staff_members),
        'gov_officials': gov_officials,
        'gov_officials_count': len(gov_officials),
        'project_list': project_list,
        'project_comment_list': project_comment_list,
    }
    

    return render(request,'Operations/homepage.html', context)
 
def projects(request):
    project_list = Project.objects.all()
    
    for project in project_list:
        project_comment_list = PublicComment.objects.all().filter(project=project)

    for comment in project_comment_list:
        print(comment)
    
    context = {
        'project_list': project_list,
        'project_comment_list': project_comment_list,
    }
    return render(request,'Operations/projects.html', context)

def view_updates(request):
    return render(request,'Operations/updates.html')
def anouncement(request):
    return render(request,'Operations/anouncements.html')

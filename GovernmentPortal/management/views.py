from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from Operations.models import CabinetMember

# Create your views here.
def admin_page(request):
    user = request.user
    if user.is_authenticated and user.is_superuser:
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
        }
        message = "welcome " + str(user.first_name)
        messages.success(request, message)
        return render(request, 'management/admin.html', context)

       
    else:
        messages.success(request, "Error!, you do not have access to this page")
        return redirect('homepage')
        
    
   
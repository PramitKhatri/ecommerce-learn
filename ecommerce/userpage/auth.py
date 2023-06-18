from django.shortcuts import redirect

# check if user is logged or not

def unauthenticated_user(view_dunction):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_authentiacted:
            return redirect('/')
        else:
            return view_dunction(request, *args,**kwargs)
    return wrapper_function


# redirect user according to role if user is admin then redirect ro admin otherwise dashboard redirect to normal user page
def admin_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return view_function(request,*args,**kwargs)
        else:
            return redirect('/')
    return wrapper_function
from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps
from django.shortcuts import redirect

def user_authenticated(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            if user.groups.filter(name='client').exists():
                return redirect('client')
            elif user.groups.filter(name='admin').exists():
                print("decorator khdam")
                return redirect('AdminPage')
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view


def allowed_users(allowed_roles=[]):
  def decorator(view_func):
    def wrapper_func(request, *args, **kwargs):
      group = None
      if request.user.groups.exists():
        group = request.user.groups.all()[0].name
      if group in allowed_roles:
        return view_func(request, *args, **kwargs)
      else :  
        user = request.user
        if user.groups.filter(name='client').exists():
            return redirect('client')
        elif user.groups.filter(name='admin').exists():
            return redirect('AdminPage')
        
    return wrapper_func
  return decorator
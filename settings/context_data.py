from .models import Setting

def get_context_data(request):
    data=Setting.objects.last()
    return {'context_data':data}
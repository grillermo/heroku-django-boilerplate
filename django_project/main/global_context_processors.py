from main.utils import get_full_path

def basics(request):
    context = {}
    context['current_url'] = get_full_path(request)
    return context


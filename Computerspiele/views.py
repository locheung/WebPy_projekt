from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from .forms import ComputerspielForm
from .models import Computerspiel

# -------------------------------------------------------------------------------

# class SpielListView(ListView):
#     model = Computerspiel
#     context_object_name = 'alle_spiele'  # Default: object_list
#     template_name = 'spiel-list.html'  # Default: computerspiel_list.html

def function_based_view_spiel_list(request):
    print_var_alle_spiele = Computerspiel.objects.all()
    print(print_var_alle_spiele)
    context = {'alle_spiele' : print_var_alle_spiele}
    return render(request, 'spiel-list.html', context)

# -------------------------------------------------------------------------------

# class SpielDetailView(DetailView):
#     model = Computerspiel
#     context_object_name = 'dieses_spiel'  # Default: computerspiel
#     template_name = 'spiel-detail.html'  # Default: computerspiel_detail.html

def function_based_view_spiel_detail(request, **kwargs):
    spiel_id = kwargs['pk']
    print_var_dieses_spiel = Computerspiel.objects.get(id=spiel_id)
    print(kwargs)
    print(str(spiel_id), ' : ', print_var_dieses_spiel)
    context = {'dieses_spiel' : print_var_dieses_spiel}
    return render(request, 'spiel-detail.html', context)

# -------------------------------------------------------------------------------

# class SpielCreateView(CreateView):
#     model = Computerspiel
#     form_class = ComputerspielForm
#     template_name = 'spiel-create.html'  # Default: computerspiel_form.html
#     success_url = reverse_lazy('spiel-list')

#     def form_valid(self, form):
#         form.instance.ersteller = self.request.user
#         return super().form_valid(form)

def function_based_view_spiel_create(request):
    if request.method == 'POST':
        print('du bist in HTTP methode POST')
        form_in_meinem_function_based_view = ComputerspielForm(request.POST)
        form_in_meinem_function_based_view.instance.ersteller = request.user

        if form_in_meinem_function_based_view.is_valid():
            print('neues Spiel gespeichert')
            form_in_meinem_function_based_view.save()

        else:
            print(form_in_meinem_function_based_view.errors)
            pass
        return redirect('spiel-list')

    else:  # jetzt bist du in request.method == 'GET'; führt dich zum formular zum ausfüllen
        print('du bist in HTTP methode GET')
        form_in_meinem_function_based_view = ComputerspielForm()
        context = {'form' : form_in_meinem_function_based_view}
        return render(request, 'spiel-create.html', context)

# -------------------------------------------------------------------------------

# class SpielDeleteView(DeleteView):
#     model = Computerspiel
#     context_object_name = 'dieses_spiel_loeschen'
#     template_name = 'spiel-confirm-delete.html'  # Default: computerspiel_check_delete.html
#     success_url = reverse_lazy('spiel-list')

def function_based_view_spiel_delete(request, **kwargs):
    context = {}
    if request.method == 'POST':
        print('du bist in method == POST')
        spiel_id = kwargs['pk']
        zu_loeschendes_spiel = Computerspiel.objects.get(id=spiel_id)
        print(zu_loeschendes_spiel, ': spiel wird gelöscht')
        zu_loeschendes_spiel.delete()
        print('spiel gelöscht')
        return redirect('spiel-list')
    return render(request, 'spiel-confirm-delete.html', context)
from django.shortcuts import get_object_or_404, render

from django.views.generic import TemplateView

from .models import ContactData



def homepage(request):

  context = {
    "contact_list": ContactData.objects.all(),
  }

  return render(request, 'contactus/homepage.html', context=context)



def functionv(request,id):

  context={
    "contact": get_object_or_404(ContactData, pk=id),
  }

  return render(request, 'contactus/functionv.html', context=context)



class classv(TemplateView):
  template_name = 'contactus/classv.html'

  def get(self,request,id):
    contact = get_object_or_404(ContactData, pk=id)
    context={
      "contact":contact,
    }
    return render(request, self.template_name, context=context)


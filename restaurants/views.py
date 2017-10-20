from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from .forms import *

# Create your views here.

def restaurant_createview(request):
	template_name = 'restaurants/form.html'
	context = {}
	return render(request, template_name, context)



# def restaurant_list(request):
# 	template_name = 'restaurants/restaurants_list.html'
# 	queryset = Restaurant.objects.all()
# 	context = {
# 		'object_list': queryset
# 	}
# 	return render(request, template_name, context)

class RestaurantListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get('slug')
		if slug:
			queryset = Restaurant.objects.filter(
					Q(category__iexact=slug) |
					Q(category__icontains=slug)
				)
		else:
			queryset = Restaurant.objects.all()

		return queryset

class RestaurantDetailView(DetailView):
	queryset = Restaurant.objects.all()

	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(Restaurant, id=rest_id)
	# 	return obj


	
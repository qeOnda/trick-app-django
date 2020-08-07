from django.forms import ModelForm, Select, BooleanField
from .models import To_learn, Category


# choices = [('flip', 'flip'), ('grind', 'grind'), ('slide', 'slide'), ('manual', 'manual')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for choice in choices:
	choice_list.append(choice)

class TrickForm(ModelForm):
	class Meta:
		model = To_learn
		exclude = ['learned']
		widgets = {
			'category': Select(choices=choice_list, attrs={'class': 'form-control'})
		}

class LearnForm(ModelForm):
	learned = BooleanField(initial=False, required=False)

	class Meta:
		model = To_learn
		fields = ['learned']

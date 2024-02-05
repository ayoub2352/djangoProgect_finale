import django_filters
from .models import *


class VoyageFilter(django_filters.FilterSet):
    date_depart = django_filters.DateFilter(field_name='date_depart', lookup_expr='gte')
    date_arrivee = django_filters.DateFilter(field_name='date_depart', lookup_expr='lte')
    classe_vol = django_filters.ChoiceFilter(choices=Vol.CLASSE_CHOICES, field_name='vol__classe', label='Classe de vol')
    nombre_etoiles_hotel = django_filters.ChoiceFilter(choices=Hotel.NBR_ETOILE, field_name='hotel__nbr_etoiles', label='Nombre d\'étoiles d\'hôtel')
    ville_depart = django_filters.CharFilter(field_name='vol__ville_depart', label='Ville de départ')
    ville_arrive = django_filters.CharFilter(field_name='vol__ville_arrive', label='Ville d\'arrivée')

    class Meta:
        model = Voyage
        fields = ['titre', 'date_depart', 'date_arrivee', 'classe_vol', 'nombre_etoiles_hotel', 'ville_depart', 'ville_arrive']
        exclude = ['image_voyage']



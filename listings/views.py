from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Listing
from django.db.models import Q, Sum, Case, When, IntegerField, F
from .serializers import ListingSerializer, ListingDetailSerializer
from datetime import datetime, timezone, timedelta
import functools

class ListingsView(ListAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer
    lookup_field = 'slug'

class ListingView(RetrieveAPIView):
    queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
    serializer_class = ListingDetailSerializer
    lookup_field = 'slug'

class SearchView(APIView):
    def post(self, request, format=None):
        queryset = Listing.objects.order_by('-list_date').filter(is_published=True)
        data = self.request.data

        for field, value in data.items():
            if field == 'sale_type':
                queryset = queryset.filter(sale_type__iexact=value)
            elif field == 'price':
                price = self.convert_price_range(value)
                if price is not None:
                    queryset = queryset.filter(price__lte=price)
            elif field == 'bedrooms':
                bedrooms = int(value.rstrip('+'))
                queryset = queryset.filter(bedrooms__gte=bedrooms)
            elif field == 'home_type':
                queryset = queryset.filter(home_type__iexact=value)
            elif field == 'bathrooms':
                bathrooms = float(value.rstrip('+'))
                queryset = queryset.filter(bathrooms__gte=bathrooms)
            elif field == 'sqft':
                sqft = self.convert_sqft(value)
                if sqft is not None:
                    queryset = queryset.filter(sqft__lte=sqft)
            elif field == 'days_listed':
                days_passed = self.convert_days_listed(value)
                if days_passed is not None:
                    queryset = queryset.filter(list_date__gte=timezone.now() - timezone.timedelta(days=days_passed))







            elif field == 'open_house':
                open_house = self.convert_open_house(value)
                if open_house is not None:
                    queryset = queryset.filter(open_house__iexact=open_house)
            elif field == 'keywords':
                queryset = queryset.filter(desc__icontains=value)

        serializer = ListingSerializer(queryset, many=True)
        return Response(serializer.data)

    def convert_price_range(self, price_str):
        if price_str == 'Any':
            return None
        elif price_str.endswith('+'):
            return int(price_str.replace('+', '').replace(',', ''))
        else:
            return None

    def convert_sqft(self, sqft_str):
        if sqft_str == 'Any':
            return None
        elif sqft_str.endswith('+'):
            return int(sqft_str.replace('+', '').replace(',', ''))
        else:
            return None

    def convert_days_listed(self, days_listed_str):
        if days_listed_str == 'Any':
            return None
        elif ' or less' in days_listed_str:
            return int(days_listed_str.split(' ')[0])
        else:
            return None

    def convert_open_house(self, open_house_str):
        if open_house_str.lower() in ['true', 'false']:
            return open_house_str.lower()
        else:
            return None
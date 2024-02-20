from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Rest
from .serializers import RestSerializer

# Create your views here.

class RestList(ListCreateAPIView):
    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    queryset = Rest.objects.all()

    #serializing
    serializer_class = RestSerializer

# The ThingDetail needs the same things
class RestDetail(RetrieveUpdateDestroyAPIView):
    queryset = Rest.objects.all()
    serializer_class = RestSerializer

from rest_framework import viewsets, status, filters, permissions
from django.shortcuts import render, redirect
from .forms import CongeEmployeForm, CongeDirigeantForm
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employe, Dirigeant, Conge
from .serializers import EmployeSerializer, DirigeantSerializer, CongeSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

class BaseViewSet(viewsets.ModelViewSet):
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['poste', 'date_embauche']
    ordering_fields = ['nom', 'prenom', 'date_embauche']
    permission_classes = [permissions.IsAuthenticated]

class DirigeantViewSet(viewsets.ModelViewSet):
    queryset = Dirigeant.objects.all()
    serializer_class = DirigeantSerializer
    permission_classes = [permissions.IsAdminUser]

class CongeViewSet(viewsets.ModelViewSet):
    queryset = Conge.objects.all()
    serializer_class = CongeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['employe', 'type_conge', 'statut']
    ordering_fields = ['date_debut', 'date_fin']

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

def demande_conge(request):
    if request.method == 'POST':
        if Dirigeant.objects.filter(employe__user=request.user).exists():
            form = CongeDirigeantForm(request.POST)
        else:
            form = CongeEmployeForm(request.POST)

        if form.is_valid():
            conge = form.save(commit=False)
            conge.employe = request.user
            conge.save()
            return redirect('liste_conges')
    else:
        if Dirigeant.objects.filter(employe__user=request.user).exists():
            form = CongeDirigeantForm()
        else:
            form = CongeEmployeForm()

    return render(request, 'demande_conge.html', {'form': form})

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

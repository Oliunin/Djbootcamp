from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import My_user
from AppTwo.forms import NewUserForm
from AppTwo.models import Company
from AppTwo.models import House
from rest_framework.response import Response
from rest_framework import generics
from AppTwo.serializers import HouseSerializer, CompanySerializer


# Create your views here.
def index(request):
    my_dict = {'insert_me':"Hello I'm from AppTwo/views.py"}
    return render(request,'AppTwo/index.html',context=my_dict)

def help(request):
    my_dict = {'help':'help page'}
    return render(request,'AppTwo/help.html',context=my_dict)

def users(request):
    userslist = My_user.objects.order_by('u_email')
    users_dict = {'userslist':userslist}
    return render(request,'AppTwo/users.html',context=users_dict)

# def Complist(request):
#      complist = Company.objects.order_by('-comp_house_count')[:10]
#      # houselist = House.objects.filter(comp_id=)
#      content={"complist":complist,}
#      return render(request,'Apptwo/map.html',content)


# def Houseview(request,pk):
#     Houselist = House.objects.filter(comp_id=pk)
#     content={"houselist":houselist}
#     return render(request,'AppTwo/map.html',content)

def NewUser(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print("fprm NewUserForm, method POST")
        if form.is_valid():
            form.save(commit=True)
            return index(request)
            print("FORM valid and verified and data commited")
        else:
            print('INVALID FORM')
    return render(request,'AppTwo/register.html',{'form':form})

class gethouses(generics.ListAPIView):
    """
    Returns a list of all houses
    """
    def get(self, request):
        Houses = House.objects.all()
        # Companies = Company.objects.all()
        HSerializer = HouseSerializer(Houses, many=True)
        # CSerializer = CompanySerializer(Companies, many=True)
        return Response({"Houses": HSerializer.data})

class getcompanies(generics.ListAPIView):
    """
    Returns a list of all companies
    """
     # model = Company
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # def get(self, request):
    #     Companies = Company.objects.all()
    #     # Companies = Company.objects.all()
    #     CSerializer = CompanySerializer(Companies, many=True)
    #     # CSerializer = CompanySerializer(Companies, many=True)
    #     return Response({"Companies": CSerializer.data})

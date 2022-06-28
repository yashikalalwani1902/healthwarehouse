from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from app.models import Profile, Medicine, Orders, Review
from django.http.response import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from app.myserializer import MedicineSerializer, OrderSerializer,\
    ReviewSerializer
from django.db.models.query import QuerySet
from django.db.models import Q


# Create your views here.
class IndexView(TemplateView):
    template_name = "app/index.html"
    
class AboutView(TemplateView):
    template_name = "app/about.html"
    
class ContactView(TemplateView):
    template_name = "app/contact.html"
    
def contactform(req):
    name = req.POST.get('name')
    email = req.POST.get('email')
    phone = req.POST.get('phoneno')
    msg = req.POST.get('msg')
    sub = " Enquiry from HealthWarehouse "
    msg = "Name - " + name + ",Email - " + email + ",Phone No -  " + phone + ",Msg - " + msg
    from_em = "HealthWarehouse Admin"
    to = ['perseusmhrn@gmail.com',] 
    done = send_mail(sub,msg,from_em,to)
    if done == 0:
        return HttpResponseRedirect(redirect_to='/app/index/?msg=0')
    else:
        return HttpResponseRedirect(redirect_to='/app/index/?msg=1')


class StoreView(TemplateView):
    template_name = "app/store.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context['medicine_list'] = Medicine.objects.all()
        return context

@method_decorator(login_required,name='dispatch')
class MedicineDetailView(TemplateView):
    template_name = "app/med_detail.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        m_id = self.kwargs['id']
        med = Medicine.objects.get(id=m_id)
        context['medicine'] = med
        # print(Order.objects.filter(medicine=Medicine.objects.get(id=m_id)))
        # order_list = Order.objects.filter(medicine=Medicine.objects.get(id=m_id))
        # review_list = QuerySet()
        # for order_element in order_list:
            # review = Review.objects.filter(order=order_element)
            # review_list.append(review)
        # context['reviews'] = review_list
        order_list = Orders.objects.filter(medicine=med) 
        context['reviews'] = []
        if order_list.exists() :
            review_list = Review.objects.filter(orders__medicine=med)
            if review_list.exists():
                context['reviews'] = review_list
        return context


@method_decorator(login_required,name='dispatch')
class MedicineCartView(TemplateView):
    template_name = "app/cart.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        m_id = self.kwargs['id']
        # if qty != None:
            # print(qty)
        context['med'] = Medicine.objects.get(id=m_id)
        return context
    
    def form_valid(self):
        print(self.object)
        
def OrderMedicine(req):
    qty = req.POST.get('qty')
    m_id = req.POST.get('m_id')
    med = Medicine.objects.get(id=m_id)
    total_price = med.price * float(qty)
    # user, medicine, quantity , total_price  -> qty * med.price
    Orders.objects.create(user=req.user,medicine=med,quantity=qty,total_price=total_price)
    return HttpResponseRedirect(redirect_to="/app/orders/")

@method_decorator(login_required,name='dispatch')        
class OrdersView(TemplateView):
    template_name = "app/orders.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        if self.request.user.is_superuser:
            context['orders'] = Orders.objects.all()
        else:
            context['orders'] = Orders.objects.filter(user=self.request.user) 
        return context

@method_decorator(login_required,name='dispatch')
class OrdersReviewView(TemplateView):
    template_name = "app/order_review.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        o_id = self.kwargs['id']
        context['o'] = Orders.objects.get(id=o_id)
        return context
    
def ReviewDone(req):
    o_id = req.POST.get('o_id')
    rating = req.POST.get('rating')
    comment = req.POST.get('comment')
    Review.objects.create(order=Orders.objects.get(id=o_id),rating=rating,comment=comment)
    return HttpResponseRedirect(redirect_to="/app/index/")
 

@method_decorator(login_required,name='dispatch')    
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['bio','disease','age','full_address','contact_no']
    

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all().order_by('-id')
    serializer_class = MedicineSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer
    

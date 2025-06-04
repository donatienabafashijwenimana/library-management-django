from django.shortcuts import render,redirect
from .models import book,member,brower
from django.http import JsonResponse
from django.forms import DateInput
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.utils.timezone import now


def dashboard_view(request):
    return render(request,'dashboard.html')

class memberview(ListView):
    model=member
    template_name='members.html'
    context_object_name='result'
class add_member(CreateView):
    model=member 
    fields=['m_nid','m_fname','m_lname','p_number','m_gender','m_dob']
    template_name='memberform.html'
    success_url=reverse_lazy('members')
    
class update_member(UpdateView):
    model=member 
    fields=['m_nid','m_fname','m_lname','p_number','m_gender','m_dob']
    template_name='memberform.html'
    success_url=reverse_lazy('members')
class delete_member(DeleteView):
    model=member
    template_name='delete/deletemember.html'
    success_url= reverse_lazy('members')
def searchmember(req):
    usersearch = req.POST.get('q')
    if usersearch  and len(usersearch) >= 1:
        result= member.objects.filter(
            Q(m_fname__icontains=usersearch) | Q(m_lname__icontains=usersearch)
        )
        return render(req,'searchmember.html',{'result':result})
    else:
        data= member.objects.all()
        return render(req,'searchmember.html',{'result':result})
        
        

class bookview(ListView):
    model = book
    context_object_name = 'result'
    template_name = 'books.html'

def searchbook(request):
    usersearch = request.POST.get('q')    
    if usersearch and len(usersearch) >= 1:
        result = book.objects.filter(
            Q(book_name__icontains=usersearch) | Q(author__icontains=usersearch)
        ) 
        return render(request,'searchbook.html',{'result':result})
    else:
        result= book.objects.all()
        return render(request,'searchbook.html',{'result':result})

class add_book(CreateView):
    model=book
    fields=['book_name','author','description']
    template_name='bookform.html'
    context_object_name='data'
    success_url=reverse_lazy('books')
class updatebook(UpdateView):
   model=book
   fields=['book_name','author','description']
   template_name='bookform.html'
   success_url= reverse_lazy('books')
class deletebook(DeleteView):
    model=book
    template_name='delete/deletebook.html'
    success_url=reverse_lazy('books')
    
    
class add_brower(CreateView):
    model  = brower
    fields= ['member_id','book_id','brow_date','date_to_return']
    template_name='browerform.html'
    success_url= reverse_lazy('brower')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['member_id'].queryset = member.objects.order_by('m_fname','m_lname')
        form.fields['book_id'].queryset = book.objects.order_by('book_name','author')
        
        form.fields['brow_date'].widget=DateInput(attrs={'type':'date','readonly': 'readonly'},
                                                  format='%Y-%m-%d')
        form.fields['brow_date'].initial=now().date()
        form.fields['date_to_return'].widget=DateInput(attrs={'type':'date'},format='%Y-%m-%d')
        
        #get browed book but returned
        non_returned_book = brower.objects.filter(returned_on__isnull=True).values_list('book_id',flat=True)
        
        form.fields['book_id'].queryset=book.objects.filter(
            ~Q(id__in=non_returned_book)
        ) 
        
        return form 
    
class browerview(ListView):
    model=brower
    context_object_name='result'
    template_name='brower.html'
    def get_queryset(self):
        return brower.objects.select_related('member_id','book_id')

class updatebrower(UpdateView):
    model=brower
    template_name='browerform.html'
    fields=['member_id','book_id','brow_date','date_to_return']
    success_url=reverse_lazy('brower')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['member_id'].queryset = member.objects.order_by('m_fname','m_lname')
        form.fields['book_id'].queryset = book.objects.order_by('book_name','author')
        form.fields['brow_date'].widget = DateInput(attrs={'type': 'date','readonly': 'readonly'}, format='%Y-%m-%d')
        form.fields['date_to_return'].widget=DateInput(attrs={'type':'date'},format='%Y-%m-%d')
                
        #get browed book but returned
        non_returned_book = brower.objects.filter(returned_on__isnull=False).values_list('book_id',flat=True)

        current_book = self.object.book_id_id
        form.fields['book_id'].queryset=book.objects.filter(
            ~Q(id__in=non_returned_book) | Q(id=current_book)
        ) 
        
        return form 

class return_book(UpdateView):
    model=brower
    template_name='browerreturn.html'
    fields=['returned_on']
    success_url=reverse_lazy('brower')
    def get_form(self, form_class =None):
        form = super().get_form(form_class)
        form.initial['returned_on'] = now().date()
        form.fields['returned_on'].widget=DateInput(attrs={'type':'date','readonly':'readonly'},
                                                    format='%Y-%m-%d')
        return form
    
class delete_brower(DeleteView):
    model= brower
    template_name='delete/deletebrower.html'
    success_url= reverse_lazy('brower')

def browed_books(args):
    pass
def logout(request):
    return render(request,'logout.html')

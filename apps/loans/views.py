from datetime import date
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from .models import *
from .forms import *


class AddLoanView(FormView):
    template_name = 'loans/add_loan.html'
    form_class = LoanForm
    success_url = '.'

    def form_valid(self, form):
        """La función get or create valida si un eobjeto ya existe y lo crea, caso contrario ejecuta una redirección"""
        obj, created = Loan.objects.get_or_create(
            # Los parámetros que no forman parte del ciccionario defaults son los que se usan para validar la existencia
            # del objeto. En el diccionario default, se ingresan los demás parámetros que se usarán para registrar el objeto
            book=form.cleaned_data['book'],
            reader=form.cleaned_data['reader'],
            is_returned=False,

            defaults={
                'date_loan' :date.today(),
            }
        )

        if created:
            return super(AddLoanView, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')



class AddMultipleLoanView(FormView):
    template_name = 'loans/add_multiple_loan.html'
    form_class = LoanMultipleForm
    success_url = '.'

    def form_valid(self, form):
        """La función bulk_create crea varios registros en la base de datos"""
        
        loans = []
        for l in form.cleaned_data['books']:
            loan = Loan(
                reader=form.cleaned_data['reader'],
                book=l,
                date_loan=date.today(),
                is_returned=False
            )
            loans.append(loan)

        Loan.objects.bulk_create(loans)

        return super(AddMultipleLoanView, self).form_valid(form)


# class RegisterLoanView(FormView):
#     template_name = 'loans/add_loan.html'
#     form_class = LoanForm
#     success_url = '.'

#     def form_valid(self, form):
#         """Forma 1 de crear un registro. Se interactua con el ORM usando el método create()"""
#         # Loan.objects.create(
#         #     book=form.cleaned_data['book'],
#         #     reader=form.cleaned_data['reader'],
#         #     date_loan=date.today(),
#         #     is_returned=False
#         # )
#         """Forma 2 de crear un registro. Se crea la instancia usando el constructor y con el método save()"""
#         loan =  Loan(
#             book=form.cleaned_data['book'],
#             reader=form.cleaned_data['reader'],
#             date_loan=date.today(),
#             is_returned=False
#         )
#         loan.save()

#         """Para reslatar: La diferencia entre estoas dos formas es: que en la primera se crea la instancia desde cero
#         y en la segunda si la instancia no existe la crear, pero si existe basicamente lo que ejecuta es una actualización del objeto en cuestión"""
        
#         # book = form.cleaned_data['book']
#         # book.stock -= 1
#         # book.save()
#         return super(RegisterLoanView, self).form_valid(form)

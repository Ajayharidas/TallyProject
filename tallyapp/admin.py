from django.contrib import admin
from .models import Countries,States,Companies,Group,Features,Costcentre,Currency,Voucher,Ledger,Ledger_Mailing_Details,Ledger_Banking_Details,Ledger_Asset_Rounding,Ledger_Asset_Statutory,Ledger_Sundry,Accounting_Voucher_Creation,list_of_Vouchers_created

admin.site.register(Countries)
admin.site.register(States)
admin.site.register(Companies)
admin.site.register(Group)
admin.site.register(Features)
admin.site.register(Costcentre)
admin.site.register(Currency)
admin.site.register(Voucher)
admin.site.register(Ledger)
admin.site.register(Ledger_Mailing_Details)
admin.site.register(Ledger_Banking_Details)
admin.site.register(Ledger_Asset_Rounding)
admin.site.register(Ledger_Asset_Statutory)
admin.site.register(Ledger_Sundry)
admin.site.register(Accounting_Voucher_Creation)
admin.site.register(list_of_Vouchers_created)

# Register your models here.

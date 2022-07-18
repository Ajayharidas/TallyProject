from pyexpat import model
from django.db import models

class Countries(models.Model):
    name=models.CharField(max_length=225)
    

    
class States(models.Model):
    name=models.CharField(max_length=225)
    country=models.ForeignKey(Countries,on_delete=models.CASCADE,blank=True,null=True)
    
class Companies(models.Model):
    name=models.CharField(max_length=225)
    mailing_name=models.CharField(max_length=225)
    address1=models.CharField(max_length=225)
    address2=models.CharField(max_length=225)
    address3=models.CharField(max_length=225)
    address4=models.CharField(max_length=225)
    pincode=models.CharField(max_length=6)
    telephone=models.CharField(max_length=225)
    mobile=models.CharField(max_length=225)
    fax=models.CharField(max_length=225)
    email=models.EmailField()
    website=models.CharField(max_length=225)
    fin_begin=models.DateField(null=True)
    books_begin=models.DateField(null=True)
    state=models.ForeignKey(States,on_delete=models.CASCADE,blank=True,null=True)
    country=models.ForeignKey(Countries,on_delete=models.CASCADE,blank=True,null=True)
    currency_symbol=models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    active=models.BooleanField(default=True)
    
    
class Group(models.Model):
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225,null=True)
    under = models.CharField(max_length=225)
    sub_ledger = models.BooleanField(default=False)
    debit_credit = models.BooleanField(default=False)
    calculation = models.BooleanField(default=False)
    used_purchase = models.CharField(max_length=225,null=True,blank=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    

class Features(models.Model):
    maintain_accounts = models.BooleanField(default=True)
    bill_wise_entry = models.BooleanField(default=True)
    cost_centres = models.BooleanField(default=False)
    interest_calc = models.BooleanField(default=True)
    maintain_inventory = models.BooleanField(default=True)
    integrate_accounts = models.BooleanField(default=True)
    multiple_price_level = models.BooleanField(default=True)
    batches = models.BooleanField(default=True)
    expirydate_batches = models.BooleanField(default=True)
    joborder_processing = models.BooleanField(default=True)
    sub_ledger = models.BooleanField(default=True)
    cost_tracking= models.BooleanField(default=True)
    job_costing = models.BooleanField(default=True)
    discount_invoices = models.BooleanField(default=True)
    Billed_Quantity = models.BooleanField(default=True)
    gst = models.BooleanField(default=False)
    tds = models.BooleanField(default=False)
    tcs = models.BooleanField(default=False)
    vat = models.BooleanField(default=False)
    excise = models.BooleanField(default=True)
    servicetax = models.BooleanField(default=True)
    payroll = models.BooleanField(default=False)
    multiple_addrss = models.BooleanField(default=True)
    vouchers = models.BooleanField(default=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class Costcentre(models.Model):
    cname = models.CharField(max_length=225)
    alias = models.CharField(max_length=225,null=True)
    under = models.CharField(max_length=225)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    
class Currency(models.Model):
    symbol = models.CharField(max_length=225)
    formal_name = models.CharField(max_length=225)
    currency_code = models.CharField(max_length=225)
    decimal_places = models.CharField(max_length=225)
    show_in_millions = models.BooleanField(default=False)
    suffix_symbol = models.BooleanField(default=False)
    symbol_and_amount = models.BooleanField(default=False)
    after_decimal = models.CharField(max_length=225)
    amount_in_words = models.CharField(max_length=225)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
class Voucher(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type =  models.CharField(max_length=225)
    method_voucher_numbering = models.CharField(max_length=225)
    use_adv_conf = models.CharField(max_length=225,blank=True)
    prvnt_duplictes = models.CharField(max_length=225,default="Null",blank=True)
    use_effective_date =  models.CharField(max_length=225,default="Null")
    allow_zero_value_trns =  models.CharField(max_length=225)
    allow_naration_in_voucher =  models.CharField(max_length=225)
    make_optional =  models.CharField(max_length=225)
    provide_naration =  models.CharField(max_length=225)
    print_voucher = models.CharField(max_length=225)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    
class Ledger(models.Model):
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    under =  models.CharField(max_length=225)
    provide_banking_details =  models.CharField(max_length=225)
    pan_no=models.CharField(max_length=225)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
class Ledger_Mailing_Details(models.Model):
    mailingname = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    country =models.CharField(max_length=225)
    pincode =models.CharField(max_length=225)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, blank=True,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class Ledger_Banking_Details(models.Model):
    od_limit = models.CharField(max_length=225)
    holder_name =models.CharField(max_length=225)
    acc_no =models.CharField(max_length=225)
    ifsc =models.CharField(max_length=225)
    swift_code =models.CharField(max_length=225)
    bank_name = models.CharField(max_length=225)
    branch = models.CharField(max_length=225)
    set_cheque =  models.CharField(max_length=225)
    ch_printing =  models.CharField(max_length=225)
    ch_config= models.CharField(max_length=225)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, blank=True,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class Ledger_Asset_Rounding(models.Model):
    rounding_method =models.CharField(max_length=225)
    round_limit = models.CharField(max_length=225)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, blank=True,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    
class Ledger_Asset_Statutory(models.Model):
    assessable_calculation = models.CharField(max_length=225)
    appropriate_to =models.CharField(max_length=225)
    gst_applicable = models.CharField(max_length=225)
    set_alter_GST =models.CharField(max_length=225)
    type_of_supply = models.CharField(max_length=225)
    method_of_calc=models.CharField(max_length=225)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, blank=True,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class Ledger_Sundry(models.Model):
    maintain_balance_bill_by_bill =models.CharField(max_length=225,default="Null",blank=True)
    default_credit_period=models.CharField(max_length=225,default="Null",blank=True)
    check_for_credit_days=models.CharField(max_length=225,default="Null",blank=True)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, blank=True,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class Accounting_Voucher_Creation(models.Model):
    date = models.DateField()
    total_amount = models.CharField(max_length=255)
    narration = models.CharField(max_length=500)
    company = models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    voucher_type = models.ForeignKey(Voucher,on_delete=models.CASCADE,blank=True,null=True)
    ledger = models.ForeignKey(Ledger,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.voucher_type.voucher_type

class list_of_Vouchers_created(models.Model):
    amount = models.CharField(max_length=255)
    voucher_creation = models.ForeignKey(Accounting_Voucher_Creation,on_delete=models.CASCADE,blank=True,null=True)
    ledger = models.ForeignKey(Ledger,on_delete=models.CASCADE,blank=True,null=True)
    

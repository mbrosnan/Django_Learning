from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def index(request):
    template_name = "mcalc/index.html"
    homeprice = request.POST.get("homeprice", "")
    downpayment = request.POST.get("downpayment", "")
    loanterm = request.POST.get("loanterm", "")
    interestrate = request.POST.get("interestrate", "")
    
    if (not homeprice) or (not downpayment) or (not loanterm) or (not interestrate):
        outputText = "Fill in all boxes below to calculate your mortgage payment."
    else:
        
        loanamount = int(homeprice) - int(downpayment)
        monthlyinterestrate = float(interestrate) / 100 / 12
        numberofpayments = int(loanterm)
        monthlypayment = loanamount * (monthlyinterestrate * (1 + monthlyinterestrate) ** numberofpayments) / ((1 + monthlyinterestrate) ** numberofpayments - 1)
        
        
        outputText = "Your monthly mortgage payment is: ${:.2f}".format(monthlypayment)





    return render(
            request,
            "mcalc/index.html",
            {
                "output": outputText,
                "homeprice.value": homeprice,
            },
    )
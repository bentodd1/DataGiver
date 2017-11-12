from django.shortcuts import render
from django.http import HttpResponse
from .DataHolder import caclulateChanges
import datetime

# Create your views here.

def createCode(zip):
    code = codeStart+str(zip) +codeEnd
    return code

codeStart = 'ZILLOW/Z'
codeEnd = '_ZHVIAH'
auth = "aJyznpsDrahPb7UMRoTv"

def index(request, growth=0):
    print("In index view")
    title = "Hello"
    try:
        if 'datepicker' in request.POST:
            date = request.POST['datepicker']
            print(date)
        if 'zipCode' in request.POST:
            myZip = request.POST['zipCode']
            date = request.POST['datepicker']
            date = datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
            print(date)
            date1 = request.POST['datepicker1']
            date1 = datetime.datetime.strptime(date1, '%m/%d/%Y').strftime('%Y-%m-%d')
            print(date1)
            code=createCode(myZip)
            zipDict = caclulateChanges(title, code, auth, date, date1, 12)
            percentChange = zipDict.get("percentChange")
            zipChangeMedian = percentChange.get('median').item()
            growth = zipChangeMedian *100
            print(zipChangeMedian)
        elif 'do-something-else' in request.POST:
            print('Not Submitted')
    except:
        print('Input Failed')

    return render( request, 'RealEstate.html', {'zip': growth})
#    return HttpResponse("Welcome to Real Estate on DataGiver")
def submit(request, choice):
    if 'SendZip' in request.POST:
        print('Submitted')
    elif 'do-something-else' in request.POST:
        print('Not Submitted')


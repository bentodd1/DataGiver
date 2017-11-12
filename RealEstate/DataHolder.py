import quandl
import pandas
import matplotlib.pyplot as plt

def print_full(x):
    pandas.set_option('display.max_rows', len(x))
    print(x)
    pandas.reset_option('display.max_rows')

#  Start Date and End Date format yyyy-mm-dd
def createDataSet(code, authtokenString, startDate, endDate):
    print(startDate)
    print(endDate)
    data = quandl.get(code, authtoken=authtokenString,start_date =startDate,end_date =endDate)
    return data

def setPeriod(data,period):
    data2 =data.iloc[::period, :]
    return data2

def calcPercentChangeList(data):
    percentChangeList = data.pct_change()
    return percentChangeList

def printDataAnalysis(data, title):
    print(title)
    dict = {"mean": data.mean(),"median":data.median()}
    return dict

def caclulateChanges(title, code, authtoken, startDate, endDate,period):
    dict ={}
    #print(title)
    #print("From ", startDate, "To ",endDate )
    data = createDataSet(code, authtoken, startDate, endDate)
    data = setPeriod(data,period)
    percentChangeList =  calcPercentChangeList(data)
    percentChangeOfChangeList = calcPercentChangeList(percentChangeList)
    orig = printDataAnalysis(data,'Original Data')
    percentChange =printDataAnalysis(percentChangeList,'Percent Change')
    percentPercentChange =printDataAnalysis(percentChangeOfChangeList, 'Percent Change of Change')
    dict = {"original": orig,"percentChange":percentChange,"percentPercentChange":percentPercentChange}
    #print(dict)
    return dict

#caclulateChanges("Waldo Home Prices","ZILLOW/Z64145_ZHVIAH", "aJyznpsDrahPb7UMRoTv","2010-02-18", "2017-09-28",12)
#caclulateChanges("West Waldo Home Prices","ZILLOW/N12805_ZHVIAH", "aJyznpsDrahPb7UMRoTv","2010-01-01", "2017-09-28",12)

#quandl.get("ZILLOW/N12727_ZHVIAH", authtoken="aJyznpsDrahPb7UMRoTv")
#quandl.get("ZILLOW/N12805_ZHVIAH", authtoken="aJyznpsDrahPb7UMRoTv")





#data = quandl.get("ZILLOW/N12805_ZHVIAH", authtoken="aJyznpsDrahPb7UMRoTv",start_date="2010-01-01", end_date ="2017-09-28")
#data2 = data.iloc[::12, :]
#percentChangeList = data2.pct_change()
#percentChangeOfChange = percentChangeList.pct_change()
#print(data2.pct_change())

#print('average change ',percentChangeList.mean())
#print('median change ',percentChangeList.median())

#print('average change ',percentChangeOfChange.mean())
#print('median change ',percentChangeOfChange.median())
#data['Value'].plot();
#data.set_index('month')
#print(percentChangeList['Value'])
#print(percentChangeOfChange['Value'])
#plt.show()
#print(data.columns)
#print(data.index)
#s = data.ix[:,0]

#print(len(data.columns))
#yearlyData  = data.query('Month ==1')
#print_full(yearlyData)
#counter = 0;
#yearlyDataPoints = []
#for item in data:
#    if(counter %12 ==0):
#        yearlyDataPoints.append(item)


#print(yearlyDataPoints.pct_change())
#print_full(s)


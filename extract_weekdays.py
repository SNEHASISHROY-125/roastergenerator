import calendar, datetime

def get_month_dates(year, month):
    # Get the number of days in the specified month
    num_days = calendar.monthrange(year, month)[1]
    
    # Generate a list of dates for the entire month
    dates = [datetime.date(year, month, day) for day in range(1, num_days + 1)]
    return dates

def get_weekday_name(date):
    return date.strftime("%A")

def get_month_weekdays(year:str, month:str) -> list[str]:
    '''Get the weekdays for each day in the month'''
    _ = []
    input_year = int(year)
    input_month_number = list(calendar.month_name).index(month)   
    dates = get_month_dates(input_year, input_month_number)
    for date in dates:
        weekday = get_weekday_name(date)
        # print(f"{date.day} {date.strftime('%B')} {year}: {weekday[:3]}")
        _.append(weekday[:3])
    
    return _

# if __name__ == "main":...
# input_month = "June"
# input_year = 2023

# print(f"Dates and weekdays for {input_month} {input_year}:")
# (len(_:=get_month_weekdays(input_year, input_month)))
# print( _[:5])

'''
import format as f

#  Example
manpower = ['john doe'+'\n'+'9547709029','jim doe'+ '\n' + '95058458880','Mak ane']
designation = ['Plumber','Electrician','Carpenter']

year = '2023'
month = 'June'

save_as_file = 'Weekly roaster for '+month+year+".xlsx"

f.generate_format(month_days=_,year=year,month=month)
f.add_data(manpower=manpower,designation=designation)

# saving the workbook
f.save_workbook(file=save_as_file)
'''

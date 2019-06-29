from datetime import timedelta,time,datetime


date_now = datetime.now()

expires = date_now + timedelta(days=7)

print(date_now)
print(expires)
print (date_now < expires)
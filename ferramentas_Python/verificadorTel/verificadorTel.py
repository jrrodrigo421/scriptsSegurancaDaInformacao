import phonenumbers
from phonenumbers import timezone

phonenumber = phonenumbers.parse('+553534712908')
timezone = timezone.time_zones_for_number(phonenumber)

print(timezone)


# from phonenumbers import geocoder

# phone = input('Digite  o telefone no formato: +5535900000000: \n')

# phone_number = phonenumbers.parse(phone)

# print(geocoder.description_for_number(phone_number, 'pt'))





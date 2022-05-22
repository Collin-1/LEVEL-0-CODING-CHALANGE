def celcius_to_fahrenheit(temparature):
    fahrenheit = (temparature * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celcius(temparature):
    celcius = (temparature - 32) * 5 / 9
    return celcius


print(celcius_to_fahrenheit(0))
print(fahrenheit_to_celcius(32))

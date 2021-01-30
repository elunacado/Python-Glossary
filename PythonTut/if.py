# IF
# if name:
#else:

#ELIF = pero si
#Use AND si quieres que ambos parametros sean respetados o ignorados
#Use OR if you want to add a parameter
#bool
# name = True/False

is_male = False
is_tall = True

if is_male and is_tall:
    print("You're a male or tall or both")
elif is_male and not (is_tall):
    print("You r a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male or tall")

# Funtions with outputs🙂😎
def format_name(f_name, l_name):
    fc_name = (f_name.lower()).capitalize()
    lc_name = (l_name.lower()).capitalize()
    titled_name = fc_name + " " + lc_name
    return titled_name


f_name = input("What is your first name?")
l_name = input("What is your last name?")
final_name = format_name(f_name, l_name)
print(final_name)

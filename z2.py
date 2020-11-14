#def data_func(name, s_name, voz, proj, email, phone):


# print(f"имя - {name}; фамилия - {s_name}; год рожд - {voz};город проживания-{proj}; email-{email}; тел-{phone}")

# data_func(name=input("введите имя"), s_name=input("введите фамилию"), voz=input("год рождения"),
# proj=input("город проживания"), email=input("email"), phone=input("тел"))

# анкета
def d_f(**kwargs):
    return kwargs


print(d_f(name=input("введите имя"), s_name=input("введите фамилию"), voz=input("год рождения"),
          proj=input("город проживания"), email=input("email"), phone=input("тел")))

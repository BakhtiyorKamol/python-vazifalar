# son=float(input('Juft sonni kiriting. '))
# if son%2:
#   print("Juft sonni kiriting")
# else:
#   print("Raxmat")
# yosh=int(input("Yoshingiz nechida? "))
# if yosh<=4 or yosh>=60:
#   print('Sizga bepul')
# elif yosh<=18:
#   print('Sizga 10000 so\'m')
# else:
#   print('Sizga 20000 so\'m')
# son1=int(input("Birinchi sonni kiriting "))
# son2=int(input("Ikkinchi sonni kiriting "))
# if son1==son2:
#   print("Sonlar teng")
# elif son1>son2:
#   print(" Birinchi son katta")
# elif son1<son2:
#   print("Birinchi son kichkina")
# mahsulotlar=['sabzi','piyoz','kartoshka','qiyma','guruch','yog\'','lavlagi','sholg\'om','un','go\'sht']
# savat=[]
# bor_mahsulotlar=[]
# mavjud_emas=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} ta mahsulot kiriting>>> "))
# for zakaz in savat:
#   if zakaz in mahsulotlar:
#      print(f"{zakaz} mahsuloti do'konimizda bor")
#      bor_mahsulotlar.append(zakaz)
#   else:
#      print(f"{zakaz} mahsuloti do'konimizda yo'q")
#      mavjud_emas.append(zakaz)
# print(f"Do'konimizda {bor_mahsulotlar} mahsulotlari bor")
# print(f"Do'konimizda {mavjud_emas} mahsulotlari yo'q")
# foydalanuvchilar=['baxtiyor','Hamza','Safar','Otabek','Nurbek']
# yangi_login=input("Yangi login kiriting>>> ")
# if yangi_login.lower() in foydalanuvchilar:
#    print("Login band, yangi login tanlang!")
# else:
#    print("Xush kelibsiz!")
butun_son=int(input("Butun sonni kiritng"))
for sonlar in range(2,11):
  if not (butun_son%sonlar):
    print(f"{butun_son} qoldiqsiz {sonlar} ga bo'linadi")
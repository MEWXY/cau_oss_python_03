length = float(input("가로:"))
width  = float(input("세로:"))
height = float(input("높이:"))

#박스의 부피
volume = length * width * height

print("박스의 부피는", volume, "입니다.")


# %% 조건을 사용하여 박스의 요금 계산
total_length = length + width + height

#    80cm 이하: 5000
# 80cm   ~ 100cm: 8000
# 100cm  ~ 120cm: 10000
# 120cm  ~ 160cm: 13000
# 160cm  ~      : 배송불가
if total_length <= 80: # 80cm 이하
    charge = 5000
elif total_length <=100:
    charge = 8000
elif total_length <= 120:
    charge = 10000
elif total_length <= 160:
    charge = 13000
else:
    charge = "unavailable"

    print("Total length:", total_length)
    print("Charge:", charge)

# 과제1 사용자에게가로, 세로, 높이를입력받아박스의부피를계산하는프로그램
length = float(input("가로:"))
width = float(input("세로:"))
height = float(input("높이:"))

volume = length * width * height

print("박스의 부피는:", volume,"입니다.")

# 조건에 맞게 사용자의 박스 요금 계산 


total_length = length + width + height

if (total_length <= 80):
    charge = 5000
elif (total_length <= 100):
    charge = 8000
elif (total_length <= 120):
    charge = 10000
elif (total_length <= 160):
    charge = 13000
else:
    charge = "unknown"
print("Total Length:", total_length)
print("Charge:", charge)

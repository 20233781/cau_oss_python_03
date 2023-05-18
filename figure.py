#figure모듈은 그림과 관련된 함수 및 클래스를 제공하는 모듈이다.
#area_square, area_circle, area_regular_triangle함수로 넓이 반환
import math

class line:
    #line class는 선의 길이에 대해 저장하고 있는 클래스다
    #변수로는 외부에서 접근이 불가능한 _length가 있다
    #접근하기 위해 set_length, get_length 메소드를 제공한다.
    __length = 0
    def __init__(self, length):
        # 생성자 초기 length 값을 받는다
        # Args:
        #      length (int or float): 초기 선의 길이 값이다
        self.__length = length
    def set_length(self, length):
        #선의 길이를 수정한다.
        #Args:
        #     length (int or float): 수정하고자 하는 선의 길이다
        self.__length = length
    
    def get_length(self):
        # 객체가 정장하고 있는 선의 길이를 반환한다
        # Returns:
        #       int or float: 저장하고 있는 선의 길이 입니다
        return self.__length
def area_square(length):
        # 길이를 입력받아 정사각형의 넓이를 구하는 함수이다
        # Args:
        #      length (int or float): 한 변의 길이이다
        # Returns:
        #      int or float: 정사각형의 넓이 반환
    return length * length
def area_circle(length):
        # 길이를 입력받아 원의 넓이를 구하는 함수
        # Args:
        #      length (int or float): 반지름의 길이이다
        # Returns:
        #      int or float: 원의 넓이 반환
    return length * length * math.pi
def area_regular_triangle(length):
        # 길이를 입력받아 정삼각형의 넓이를 구하는 함수
        # Args:
        #      length (int or float): 한 변의 길이
        # Returns:
        #      int or float: 정삼각형의 넓이 반환
    return length * length * math.sqrt(3) / 4
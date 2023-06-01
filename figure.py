import math
class line:
    """
    line class는 선의 길이들에 대해 저장하고 있는 클래스다
    변수로는 접근이 불가능한 __width, __heigth가 있으며,
    해방 변수를 수정하기 위한 set_length, get_length 메소드를 제공한다
    """
    __width = 0
    __height = 0
    def __init__(self, width, height):
        """
        생성자 초기의 width와height값 입력
        Args:
            width(int or float): 초기 선의 가로 길이
            height(int or float): 초기 선의 세로 길이
        """
        self.__width = width
        self.__heigth = height
    def set_length(self, width, height):
        """
        선의 길이 수정
        Args:
            width(int or float): 수정하고자 하는 가로 길이
            height(int or float): 수정하고자 하는 세로 길이
        """
        self.__width = width
        self.__heigth = height
    def get_length(self):
        """
        객체가 저장하고 있는 선의 길이 반환
        Returns:
            int or float: 저장하고 있는 서의 길이
        """
        return self.__width, self.__heigth 
    
    def area_rectangle(width, height):
        """
        길이를 받아 직사각형 넓이를 구하는 함수
        Args:
            width(int or float): 밑변의 길이
            height(int or float): 높이의 길이
        """
        if width <= 0 or height <= 0: raise ValueError
        return width * height
    def area_ellipse(width, height):
        """
        길이를 입력받아 타원의 넓이를 구하는 함수
        Args:
            width(int or float): 짧은쪽 반지름의 길이
            height(int or float): 긴쪽 반지름의 길이
        Returns:
            int or float: 원의 넓이 반환
        """
        if width <= 0 or height <= 0: ValueError
        return width * height * math.pi
    def area_right_triangle(width, height):
        """
        길이를 입력받아 직삼각형의 넓이를 구하는 함수
        Args:
            width(int or float): 밑변의 길이
            height(int or float): 높이의 길이
        Returns:
            int or float: 직삼각형의 넓이 반환
        """
        if width <= 0 or height <= 0: raise ValueError
        return width * height / 2
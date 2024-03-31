class MySubtraction():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def execute(self):
        list_result = []
        if self.a>self.b:
            for i in range(self.b, self.a):
                list_result.append(True)
                result+=1
                
        elif self.b>self.a:
            for i in range(self.b, self.b):
                result+=1
            result = -result
        else: 
            return 0
        return result

if __name__ == '__main__':
    assert MySubtraction(1, 1).execute() == 0
    assert MySubtraction(1, 2).execute() == -1
    assert MySubtraction(2, 1).execute() == 1
    assert MySubtraction(-2, -2).execute() == 0
    assert MySubtraction(-2, 1).execute() == -3
    assert MySubtraction(1, -2).execute() == 3
    
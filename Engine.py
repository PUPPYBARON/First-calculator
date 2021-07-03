
class Engine():
    def __init__(self):
        print("Engine has been started")
    
    def compute(self,memory,memory2,a_sigh):
        if a_sigh == '+':
            answer = memory + memory2 
        elif a_sigh == '-':
            answer = memory - memory2
        elif a_sigh == '/':
            answer = memory / memory2
        elif a_sigh == 'x':
            answer = memory * memory2
        else:
            print("ERROR")
        return answer 
    


class Engine():
    def __init__(self):
        print("Engine has been started")
    
    def compute(self,memory,a_sigh):
        if a_sigh == '+':
            answer = memory + memory 
        elif a_sigh == '-':
            answer = memory - memory
        elif a_sigh == '/':
            answer = memory / memory
        elif a_sigh == 'x':
            answer = memory * memory
        else:
            print("ERROR")
        return answer 
    
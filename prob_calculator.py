import copy
import random
# Consider using the modules imported above.

class Hat:
    #Transforma um dict (kwargs) em uma lista contendo seus valores passados, exemplo: `{"red" : 1, "blue" : 2}` -> `["red","blue","blue"]`
    def __init__(self,**kwargs) -> None:
        self.contents = []
        for k,v in kwargs.items():
            for i in range(1 if v == 0 else v):
                self.contents.append(k)

    #Remove bolas aleatorias
    def draw (self, balls):
        if balls > len(self.contents):
            return self.contents
        
        else:
            #Técnica usada list comprehension
            balls_removed = [
                self.contents.pop(
                    random.randrange(
                        len(self.contents)
                    )
                )
                for i in range(balls)
            ]
                
            return balls_removed
                

#Função para verificar se a quantidade de bolas removidas é menor que a expectativa 
def _validation (expected_balls,balls_draw):
    for k,v in expected_balls.items():
        if balls_draw.count(k) < v:
            return False
    return True
        
#Função para realizar a validação do teste
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count=0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_removed = hat_copy.draw(num_balls_drawn)    
        count += int(_validation(expected_balls,balls_removed))

    return count / num_experiments
        
        


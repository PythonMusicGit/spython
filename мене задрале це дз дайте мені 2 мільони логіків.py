class Widget():
	def __init__(self, text, x, y):
        self.text=text
        self.x=x
        self.y=y
    
    def print_status(self):
        print('Napis:', self.text)
        print('Roztashuvannia',self.x,self.y)
class Button(Widget):
    def __init__(self,text,x,y,is_clicked):
        
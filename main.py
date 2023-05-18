import cv2
import mediapipe as mp
import trackingmodule as tm
from trackingmodule import handDetector

cap = cv2.VideoCapture(0)

cap.set(3,1200)
cap.set(4,720)

detector =handDetector(detectionConfidence=0.85)
keys = [["Q","W","E","R","T","Y","U","I","O","P"],
        ["A","S","D","F","G","H","J","K","L",";"],
        ["Z","X","C","V","B","N","M",",",".","/"]]

    
def drawAll(img, buttonList ):
    for button in buttonList:
        x,y = button.pos
        w,h = button.size
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),cv2.FILLED)
        cv2.putText(img,button.text,(button.pos[0]+24, button.pos[1]+61),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
    
    return img  #keep rewriting on the image frames thereby keep displaying 



class Button():
    def __init__(self,pos,text, size = (80,80)):
        self.pos = pos
        self.text = text
        self.size = size
       

        '''
        #no need to initialize again and again, making a global function to call and draw
        x,y = self.pos
        w,h = self.size
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),cv2.FILLED)
        cv2.putText(img,self.text,(self.pos[0]+24, self.pos[1]+61),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
        
        '''
        

#function that will make the keyboard buttoms
buttonList = []


#myButton = Button((100,100),"Q")

for i in range(len(keys)):
        for j,key in enumerate(keys[i]):
            buttonList.append(Button((100*j+50,100*i+50),key))

while True:
    success,img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    #making keyboard buttons using hardcoded openCV
    #cv2.rectangle(img,(100,100),(200,200),(255,0,255),cv2.FILLED)
    #cv2.putText(img,"Q",(120,175),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)

    #img  = myButton.draw(img) 
    
    #testing
    '''
    for x,key in enumerate(keys[0]):
        buttonList.append(Button((100*x + 50 ,100),key))
    for x,key in enumerate(keys[1]):
        buttonList.append(Button((100*x + 65 ,200),key))
    for x,key in enumerate(keys[2]):
        buttonList.append(Button((100*x + 75 ,300),key))
    '''


    img = drawAll(img,buttonList)



    cv2.imshow("Window",img)
    cv2.waitKey(1)
 

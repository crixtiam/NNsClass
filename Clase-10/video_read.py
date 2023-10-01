import cv2 as cv


class LeerFormato():
    def __init__(self, ruta,extension):
        self.ruta=ruta
        self.extension= extension


#class Imagen(LeerFormato):
#    def __init__(self,nombre_clase):
#        self.nombre_clase=nombre_clase
#        super().__init__(ruta,extension)
#    def read_image():






class LeerVideo():
    def __init__(self, link,nom_ventana="",tecla_salida="q"):
        self.link_video=link
        self.nom_ventana=nom_ventana
        self.tecla_salida=tecla_salida
    
    def video_read(self):
        video_capture = cv.VideoCapture(self.link_video)
        if not video_capture.isOpened():
            print("couldnt open")
            exit()
        while True:
            ret,frame = video_capture.read()
            print(frame[0])
            print(ret)
            if not ret:
                break
            
            cv.imshow(self.nom_ventana,frame)

            if cv.waitKey(25) & 0xFF == ord(self.tecla_salida):
                break
        video_capture.release()
        cv.destroyAllWindows()







human_video = LeerVideo("./dataset/human_2.mp4",nom_ventana="Human Video Clase 10")

human_video.video_read()










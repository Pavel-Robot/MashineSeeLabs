import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# код для VS иначе не дает посмотреть картинки интерактивно
import matplotlib
matplotlib.use('TkAgg',force=True)
from matplotlib import pyplot as plt
print("Switched to:",matplotlib.get_backend())
######


# Загружаю видео
video = cv.VideoCapture('test.mp4')


# Создайте цикл, чтобы пройти через каждый кадр видео. 
# Для каждого кадра примените алгоритм поиска шаблона с 
# помощью функции cv2.matchTemplate.
while True:
    # Читаем кадр
    ret, frame = video.read()
    if not ret:
        break
    # переводим кадр в оттенки серого
    gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Загрузим предварительно обученный классификатор Haar Cascade, встроенный в OpenCV
    # для обнаружения лиц
    face_classifier = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

    cv.imshow(
        "Ищу людей", frame
    ) 
    
    # Ждем нажатия клавиши "q" для выхода
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# Освобождаем ресурсы и закрываем окна
video.release()
cv.destroyAllWindows()
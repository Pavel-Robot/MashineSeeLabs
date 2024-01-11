import cv2

from PIL import Image, ImageDraw, ImageFont

# Загрузка изображения
image = cv2.imread('test_image4.jpg')

print(f"size image:{image.shape}")

# Размеры изображения (большое окно)
X, Y = image.shape[0], image.shape[1]


# фунция принимающая на вход координаты начала окна и возвращающая по трем каналам RGB среднюю яркость
def func(x, y, image):

    # Размер скользящего окна от x до width по горизонтали и от y до height по вертикали / (маленькое окно)
    width = 38 # 1024/8
    height = 51 # 768/8

    # Выделение прямоугольной части изображения
    window = image[x:x+width, y:y+height]

    # Разделение прямоугольной части на каналы RGB
    red_channel = window[:,:,2]
    green_channel = window[:,:,1]
    blue_channel = window[:,:,0]
    
    # Вычисление средней яркости каждого канала
    red = red_channel.mean()
    green = green_channel.mean()
    blue = blue_channel.mean()

    '''
    print(f"\nloc: {[x, x+width]} {[y, y+height]}")
    print("Red channel:", red)
    print("Green channel:", green)
    print("Blue channel:", blue)
    '''
    return red, green, blue

# функция для рисования, размещения блоков окна вход переменные точек прямоугольника выход
def ddrw(s_draw, s):

    img = Image.open("test_image4.jpg")

    # Создание объекта для рисования
    draw = ImageDraw.Draw(img)

    text_number = -1
    # Рисование прямоугольников
    for i in s_draw:
        draw.rectangle([(i[3], i[1]), (i[2], i[0])], outline="red")
        text_number+=1
        # Определяем координаты и параметры текста
        text = "n:" + str(text_number) + "\nb:" + str(round(s[text_number]//1))
        #text = str(text_number)
        text_color = (5, 41, 245)
        text_font = ImageFont.truetype("tahoma.ttf", 10)
        x_min, y_min, x_max, y_max = draw.textbbox(xy=(i[0],i[2]), text=text, font=text_font)
        #(x_min, y_min, x_max, y_max)

        # Рисуем текст по центру прямоугольника
        draw.text((((y_min+y_max)//2), ((x_min+x_max)//2)), text, font=text_font, fill=text_color)




    # Сохранение измененного изображения
    img.save("new_image.jpg")

s = []
drawing_point = []
for i in range(5):
    for j in range(5):
        a, b = 38*i, 51*j
        obj = func(a, b, image)
        s.append(sum(obj))
        #print(s[-1])


        drawing_point.append([a, 38*(i+1), b, 51*(j+1)])

ddrw(drawing_point, s)    

ind = s.index(max(s)) #индекс изображения
print("Окно:", ind, " Блик равен:", max(s))
print(f"Блик находится тут:\nпо y с {drawing_point[ind][0]}p по {drawing_point[ind][1]}p \nпо x с {drawing_point[ind][2]}p по {drawing_point[ind][3]}p ")




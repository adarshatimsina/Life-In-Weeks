from PIL import Image, ImageDraw
from datetime import datetime, timedelta

# code used for scanning information from the user.
def weeks_lived():
    birth_year = int(input("Enter your birth year: "))
    birth_month = int(input("Enter your birth month: "))
    birth_day = int(input("Enter your birth day: "))
    birthdate = datetime(birth_year, birth_month, birth_day) 
    today = datetime.now()
    delta = today - birthdate
    return int(delta.days / 7)

weeks_lived = weeks_lived()
print("You have lived for {} weeks".format(weeks_lived))
life_exp = int(input("Enter your region life expectancy:"))
weeks_left = ((life_exp * 52)- weeks_lived)
print(weeks_left)

# Create an image with a white background
width = 52
height = (weeks_lived + weeks_left) // 52 + 1
image = Image.new('RGB', (width * 10, height * 10), color = (255, 255, 255))
draw = ImageDraw.Draw(image)

# Draw red squares to represent the total number of weeks lived
for i in range(weeks_lived):
    x = (i % 52) * 10
    y = (i // 52) * 10
    draw.rectangle([(x, y), (x + 8, y + 8)], fill='red')

# Draw white squares to represent the total number of weeks left
for i in range(weeks_left):
    x = ((i + weeks_lived) % 52) * 10
    y = ((i + weeks_lived) // 52) * 10
    draw.rectangle([(x, y), (x + 8, y + 8)], fill='#a9a9a9')

# Save the image to a file
image.save("C:\\Users\\ASUS\\Desktop\\weeks_left.png") #change location of the directory to save the image to.
print("succesfully saved")



from PIL import Image
import random
#this import allows us to open and modify images in python
#960x640 is the blank jpeg image resolution

def main():
    size = int(input("Please enter a size for your maps: "))
    blank_image = create_image(size)
    blank_image.show()
    blank_image_pixels = blank_image.load()
    create_heightmap(blank_image_pixels, size)
    
    blank_environment_map = create_image(size)
    blank_environment_map_pixels = blank_environment_map.load()
    create_environment_map(blank_image_pixels, blank_environment_map_pixels, size)

    complex_heightmap = create_image(size)
    complex_heightmap_pixels = complex_heightmap.load()
    create_complex_heightmap(complex_heightmap_pixels,size)
    
    
    blank_image.show()
    blank_environment_map.show()
    complex_heightmap.show()


def create_image(size):
    
    blank_image = Image.new("RGB", (size,size)) # this accesses a blank image provided within the file.
    return blank_image
    

def create_heightmap(blank_image_pixels, size):
    r = 128
    for x in range(0,size): #639
        for y in range(0,size): #959
            #environment = decide_environment()
            #this function needs to be changed to use individual r,g,b values.
            increment_actual_value = (random.randint(-10,10) / 9)
            
            if r > 255 and increment_actual_value < 0:
                r += increment_actual_value
                passed_value = round(r)
                blank_image_pixels[y,x] = (passed_value,passed_value,passed_value)
            elif r < 3 and increment_actual_value > 0:
                r += increment_actual_value
                passed_value = round(r)
                blank_image_pixels[y,x] = (passed_value,passed_value,passed_value)
                
            elif r > 3 and r < 255:
                r += increment_actual_value
                passed_value = round(r)
                blank_image_pixels[y,x] = (passed_value,passed_value,passed_value)

            

            
def create_environment_map(blank_image_pixels, blank_environment_map_pixels, size):
    for x in range(0,size):
        for y in range(0,size):
            height = blank_image_pixels[x,y]
            #this complex tree of if statements finds which increment of 32 the heightmap is within, and assigns the value an rgb value based on 
            #environment that is within the height.
            #black is high mountains
            #dark purple represents forested mountains
            #pink represents forested hills
            #green represents hills
            #orange represents sage desert
            #yellow represents sandy desert
            #brown represents tropical beach
            #blue represents ocean
            if height[0] > 128:
                if height[0] > 192:
                    if height[0] > 224:
                        blank_environment_map_pixels[x,y] = (256,256,256) #this is black and represents a high mountain biome
                    else:
                        blank_environment_map_pixels[x,y] = (48,25,42) #this is purple and represents forested mountains
                    
                else:
                    if height[0] > 160:
                        blank_environment_map_pixels[x,y] = (255,105,180) #this is hot pink and represents forested hills
                    else:
                        blank_environment_map_pixels[x,y] = (144, 238, 144) #this is green and represents hills
                pass
            else:
                if height[0] > 64:
                    if height[0] > 96:
                        blank_environment_map_pixels[x,y] = (255, 165, 0) #this is orange and represents sage desert
                    else:
                        blank_environment_map_pixels[x,y] = (255,255,0) #this is yellow and represents sandy desert
                else:
                    if height[0] > 32:
                        blank_environment_map_pixels[x,y] = (165, 42, 42)#this is brown and  represents tropical beach 
                    else:
                        blank_environment_map_pixels[x,y] = (0,255,255) #this is blue and represents ocean

def create_complex_heightmap(blank_image_pixels,size):
    r = 128
    for x in range(0,size): #639
        for y in range(0,size): #959
            #environment = decide_environment()
            #this function needs to be changed to use individual r,g,b values.
            if r > 128:
                if r > 192:
                    if r > 224:
                        increment = (random.randint(-10,10) / 9)
                    else:
                        increment = (random.randint(-10,10) / 8)
                    
                else:
                    if r > 160:
                        increment = (random.randint(-10,10) / 7)
                    else:
                        increment = (random.randint(-10,10) / 6)
                pass
            else:
                if r > 64:
                    if r > 96:
                        increment = (random.randint(-10,10) / 5)
                    else:
                        increment = (random.randint(-10,10) / 4)
                else:
                    if r > 32:
                        increment = (random.randint(-10,10) / 3)
                    else:
                        increment = (random.randint(-10,10) / 2)
            
            
            if r > 255 and increment < 0:
                r += increment
                passed_value = round(r-1)
                blank_image_pixels[y,x] = (passed_value,passed_value,passed_value)
            elif r < 3 and increment > 0:
                r += increment
                passed_value = round(r)
                blank_image_pixels[y,x] = (passed_value,passed_value,passed_value)
                
            elif r > 3 and r < 255:
                r += increment
                passed_value = round(r)
                blank_image_pixels[y,x] = (passed_value,passed_value,passed_value)





            

if __name__ == "__main__":
    main()
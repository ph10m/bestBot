from PIL import Image

class ImageMod:
    def __init__(self, file=False, img=False, name=None):
        self.name = name
        self.x, self.y = 0, 0
        self.image = None
        if file:
            if name is None:
                self.name = os.path.basename(file)
            print ('Loading...',self.name)
            self.image = self.open(file)
            self.x, self.y = self.image.size
            print (self.image.size)
        elif img:
            self.image = img
            self.x, self.y = self.image.size
        else:
            self.image = None
            print('Set up an empty Image class')
            
    def setImage(self, img):
        self.image = img
        self.x, self.y = self.image.size

    def get_pixel(self,x,y): return self.image.getpixel((x,y))
    
    def getCopy(self):
        # print('Generating a copy of', self.name)
        return self.image.copy()

    def apply(self,f):
        # applies a function on each pixel (rgb)
        img = self.image.copy()
        for x in range(self.x):
            for y in range(self.y):
                img.putpixel((x,y),f(img.getpixel((x,y))))
        return img

    def keepMax(self):
        # leaves only the dominant band in each pixel
        print ('Simplifying image!')
        def f(x):
            _max = max(x)
            xD = tuple([(i if i == _max else 0) for i in x])
            # print('Colors:',xD)
            return xD
        return self.apply(f)
        
        
    def isWall(self):
        simplified = self.keepMax()
        count, r, g, b = 0,0,0,0
        for horizontal in range(0,self.x, int(self.x/10)):
            for vertical in range(0,int(self.y/2),int(self.y/5)):
                # sample every 10 pixels and get their value
                count += 1
                r,g,b = self.get_pixel(horizontal, vertical)
                if r>200:   r+=1
                elif g>200: g+=1
                else:       b+=1
        # check if either color is over-represented, thus it detects a wall (>70% of the image is covered)
        def isCovered(band,total):
            if band/total > 0.7:
                return True
            else: return False
        if isCovered(r,count) or isCovered(g,count) or isCovered(b,count):
            # this is a wall
            return True
        return False
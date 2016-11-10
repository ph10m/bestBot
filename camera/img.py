from PIL import Image

class ImageMod:
    def __init__(self, file=False, img=False, name=None):
        self.name = name
        self.x, self.y = 0, 0
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
            print('Set up an empty Image class')
			
    def getCopy(self):
        # print('Generating a copy of', self.name)
        return self.image.copy()

    def apply(self,f):
        # applies a function on each pixel (rgb)
        img = self.getCopy()
        for x in range(self.x):
            for y in range(self.y):
                img.putpixel((x,y),f(img.getpixel((x,y))))
        return img

    def keepMax(self):
        # leaves only the dominant band in each pixel
        print ('~~The winner takes it allllllllllll~~')
        def f(x):
            _max = max(x)
            return tuple([(i if i == _max else 0) for i in x])
        return self.apply(f)
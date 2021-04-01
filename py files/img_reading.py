def img_reading(img1_o,img2_o):
  img1 = cv.cvtColor(img1_o,cv.COLOR_BGR2GRAY)
  img2 = cv.cvtColor(img2_o,cv.COLOR_BGR2GRAY)
  return img1,img2
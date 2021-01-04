{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2 as cv\n",
    "import numpy as np\n",
    "from random import randint\n",
    "from PIL import Image\n",
    "\n",
    "images = ('финал.png', 'frg1.jpg', 'frg2.jpg', 'frg3.jpg', 'frg4.jpg', 'frg5.jpg', 'frg6.jpg')\n",
    "\n",
    "\n",
    "bg_cv = cv.imread(images[0])\n",
    "bg_cvpil = cv.cvtColor(bg_cv, cv.COLOR_BGR2RGB)\n",
    "bg_pil = Image.fromarray(bg_cvpil)\n",
    "\n",
    "def get_mask(bg, image):\n",
    "    rows, cols, channels = image.shape\n",
    "    roi = bg[0:rows, 0:cols]\n",
    "   \n",
    "    img2gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)\n",
    "    ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)\n",
    "    mask_inv = cv.bitwise_not(mask)\n",
    "    \n",
    "    img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)\n",
    "    img2_fg = cv.bitwise_and(image,image,mask = mask)\n",
    "    dst = cv.add(img1_bg,img2_fg)\n",
    "    return dst\n",
    "\n",
    "\n",
    "for i in range(19):\n",
    "    dst = get_mask(bg_cv, cv.imread(images[randint(1, 4)]))\n",
    "    dst = cv.cvtColor(dst, cv.COLOR_BGR2RGB)\n",
    "    dst = Image.fromarray(dst)\n",
    "    Image.Image.paste(bg_pil, dst, (randint(0,1024), randint(0,691)))\n",
    "\n",
    "out_pil = np.asarray(bg_pil)\n",
    "\n",
    "cv.imshow('res',out_pil)\n",
    "cv.waitKey(0)\n",
    "cv.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

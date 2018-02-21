import win_unicode_console
import cv2
import numpy as np
import time
import pyscreenshot as ImageGrab
from matplotlib import pyplot as plt

win_unicode_console.enable()
#   Import button 
deal_button = cv2.imread('Data\deal_button.png',0)
ok_button = cv2.imread('Data\OK_button.png',0)
start_button = cv2.imread('Data\start_button.png',0)
yes_button = cv2.imread('Data\yes_button.png',0)
no_button = cv2.imread('Data\\no_button.png',0)
high_button = cv2.imread('Data\high_button.png',0)
low_button = cv2.imread('Data\low_button.png',0)
xx_button = cv2.imread('Data\Xx.button.png',0)

#Hook function
def hook_image(img, template):
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return max_val,(top_left, bottom_right)

def hook_card():
    max_res = 0
    j1 = 0
    i1 = 0
    img2 = cv2.imread('card.png',0)
    for i in range(0,13):
        for j in range(0,4):
            result = hook_image(img2,small_cards[i][j])
            val = result[0]
            if val > max_res : 
                max_res = val
                i1 = i
                j1 = j

    if j1 == 0 : print nums[i1] + u"\u2663"
    if j1 == 1 : print nums[i1] + u"\u2666"
    if j1 == 2 : print nums[i1] + u"\u2665"
    if j1 == 3 : print nums[i1] + u"\u2660"

w, h = 13, 4
names = ['c', 'd', 'h', 's']
nums = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = [[0 for i in range(h)]for j in range(w)]
small_cards = [[0 for i in range(h)]for j in range(w)]
check = [[0 for i in range(h)]for j in range(w)]

for i in range(0,13):
    for j in range(0,4):
        card_path = 'Data' + '\\' + nums[i] + names[j] + '.png'
        # print(card_p0ath);
        cards[i][j] = cv2.imread(card_path,0)
        small_cards[i][j] = cv2.resize(cards[i][j], (77,108))
        # cv2.imshow('image', small_cards[i][j])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

if __name__ == '__main__':
    # grab fullscreen
    im = ImageGrab.grab()
    # save image file
    im.save('full_ss.png')
    img_ss = cv2.imread('full_ss.png',0)
    # Hook OK Button
    result = hook_image(img_ss,ok_button)
    x1 = result[1][0][0] - 144
    y1 = result[1][0][1] - 232
    y2 = y1 + 113
    for i in range(0,5):
        x2 = x1 + 84
        im2 = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        im2.save('card.png')
        hook_card()
        x1 = x2

    #Hook Deal Button

    im = ImageGrab.grab()
    im.save('full_ss.png')
    img_ss = cv2.imread('full_ss.png',0)
    result = hook_image(img_ss, deal_button)
    x1 = result[1][0][0]
    y1 = result[1][0][1]

    for i in range(0,5):
        x2 = x1 + 84
        im2 = ImageGrab(bbox=(x1,y1,x2,y2))
        im2.save('card.png')

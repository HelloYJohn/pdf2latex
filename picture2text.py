# @Author john-y
# @Description TODO
# @Date 2024/4/18 17:51
# @Version 1.0
import easyocr
reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
result = reader.readtext('/Users/john-y/Downloads/image/copy_bak2/IMG_2457 2.jpg')
print(result)
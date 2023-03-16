import cv2

# 读取图像文件
image_path = 'cube.png'  # 将此处替换为实际图像文件的路径
image = cv2.imread(image_path)

if image is not None:
    # 显示图像
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Failed to read image.')

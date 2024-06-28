import cv2
import numpy as np
import random

# 图片的路径
image_path = "prefiltered.jpg"

# 使用cv2.imread()函数读取图片
# 参数-1表示以图片的原始颜色格式读取图片
image = cv2.imread(image_path, cv2.IMREAD_COLOR)  # 假设图片是彩色的

# 检查图片是否正确读取
if image is not None:
    # 原始图片的大小
    original_height, original_width = image.shape[:2]

    # 定义新的分辨率大小为10x10
    new_height = original_height // 10
    new_width = original_width // 10

    # resampled_image = cv2.resize(
    #     image, (new_width, new_height), interpolation=cv2.INTER_AREA
    # )

    # resampled_image = cv2.resize(
    #     resampled_image, (original_width, original_height), interpolation=cv2.INTER_AREA
    # )

    # cv2.imwrite("prefiltered.jpg", resampled_image)

    # 计算缩放比例
    scale_x = original_width / new_width
    scale_y = original_height / new_height

    for k in range(10):
        # 创建一个10x10的空白图片
        new_image = np.zeros((new_height, new_width, 3), dtype=image.dtype)

        # 遍历新的图片的每个像素点
        for i in range(new_height):
            for j in range(new_width):
                # 计算原始图片中对应的像素点
                orig_i = int(i * scale_y + random.uniform(0, scale_y))
                orig_j = int(j * scale_x + random.uniform(0, scale_x))

                # 将原始图片的像素值赋给新的图片
                new_image[i, j] = image[orig_i, orig_j]

        # 显示原始图片和重新采样后的图片
        # cv2.imshow("Original Image", image)
        # cv2.imshow("Resampled Image", new_image)

        # 等待按键后关闭所有窗口
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # 保存重新采样后的图片
        cv2.imwrite(f"resampled_image{k}.jpg", new_image)

else:
    print("图片读取失败，请检查路径是否正确。")

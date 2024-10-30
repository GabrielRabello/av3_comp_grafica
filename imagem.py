import cv2 as cv
import numpy as np

IMG = cv.imread('dog.png', cv.IMREAD_UNCHANGED)
cv.imwrite('./imagens/original.png', IMG)


def wrapImg(img, kernelSize: int):
    w = kernelSize // 2

    fetchFirstRows = img[0: w, :]
    fetchLastRows = img[-w:, :]

    imgWrapped = img.copy()
    imgWrapped = np.insert(imgWrapped, 0, fetchLastRows, axis=0)
    imgWrapped = np.append(imgWrapped, fetchFirstRows, axis=0)

    fetchFirstCols = imgWrapped[:, 0: w]
    fetchLastCols = imgWrapped[:, -w:]
    imgWrapped = np.concatenate([fetchLastCols, imgWrapped], axis=1)
    imgWrapped = np.append(imgWrapped, fetchFirstCols, axis=1)

    return imgWrapped

def escala_cinza(imagem):
    res = np.zeros(imagem.shape, dtype=np.uint8)
    for i, j in np.ndindex(imagem.shape[:-1]):
        newRGB = int((np.int16(imagem[i, j, 0]) + np.int16(imagem[i, j, 1]) + np.int16(imagem[i, j, 2])) / 3)
        res[i, j] = [newRGB, newRGB, newRGB]

    return res

def binaria(imagem):
    max_threshold = 127
    res = np.zeros(imagem.shape, dtype=np.uint8)
    for i, j in np.ndindex(imagem.shape[:-1]):
        # Converte para escala de cinza antes
        newRGB = int((np.int16(imagem[i, j, 0]) + np.int16(imagem[i, j, 1]) + np.int16(imagem[i, j, 2])) / 3)
        if newRGB > max_threshold:
            res[i, j] = [255, 255, 255]
        else:
            res[i, j] = [0, 0, 0]

    return res

def filtro_media(imagem, wrappedImg, kernel):
    filteredImage = np.zeros(imagem.shape,dtype=np.int32)
    image_h, image_w = imagem.shape[0], imagem.shape[1]
    w = kernel//2

    for i in range(w, image_h - w): ## traverse image row
        for j in range(w, image_w - w):  ## traverse image col
            total = [0,0,0]
            for m in range(kernel):
                for n in range(kernel):
                    total += wrappedImg[i - w + m][j - w + n]
            filteredImage[i-w][j-w] = total // (kernel * kernel)
    return filteredImage


def filtro_mediana(imagem, wrappedImg, kernel: int):
    filteredImage = np.zeros(imagem.shape, dtype=np.int32)
    image_h, image_w = imagem.shape[0], imagem.shape[1]
    w = kernel // 2

    for i in range(w, image_h - w):  ## traverse image row
        for j in range(w, image_w - w):  ## traverse image col
            overlapImg = wrappedImg[i - w: i + w + 1, j - w: j + w + 1]  # Crop image for mask product
            filteredImage[i][j] = np.median(overlapImg.reshape(-1, 3), axis=0)  # Filtering

    return filteredImage

def kernel_gauss(size: int, sigma: float):
    kernel = np.zeros((size, size), dtype=np.float32)
    mean = size // 2
    for x in range(size):
        for y in range(size):
            kernel[x, y] = (1 / (2 * np.pi * sigma**2)) * np.exp(-((x - mean)**2 + (y - mean)**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)

def filtro_gaussiano(image: np.ndarray, kernel: np.ndarray):
    image_h, image_w = image.shape[:2]
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2

    # Lida com as bordas da imagem
    padded_image = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode='edge')
    filtered_image = np.zeros_like(image)

    for i in range(image_h):
        for j in range(image_w):
            # Regiao de interesse
            region = padded_image[i:i + kernel_size, j:j + kernel_size]
            # Aplica kernel
            filtered_image[i, j] = np.sum(region * kernel[:, :, np.newaxis], axis=(0, 1))

    return filtered_image

grayscale = escala_cinza(IMG)
cv.imwrite('./imagens/escala_cinza.png', grayscale)

binary = binaria(IMG)
cv.imwrite('./imagens/binaria.png', binary)

KERNEL = 5
wrapped = wrapImg(IMG, KERNEL)
ruido_media = filtro_media(IMG, wrapped, KERNEL)
cv.imwrite('./imagens/filtro_media.png', ruido_media)

ruido_mediana = filtro_mediana(IMG, wrapped, KERNEL)
cv.imwrite('./imagens/filtro_mediana.png', ruido_mediana)

gaussian_kernel_matrix = kernel_gauss(KERNEL, 1.0)

ruido_gauss = filtro_gaussiano(IMG, gaussian_kernel_matrix)
cv.imwrite('./imagens/filtro_gauss.png', ruido_gauss)

cv.waitKey(0)


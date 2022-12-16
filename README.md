# Image-Compression-and-quality-assesment
BRISQUE for Image quality assesment and SVD for image compression. In this project I have tried to compress large sized images without compromsing the quality of that image much. For testing image quality I have used BRISQUE model and for compression I have used Singular Value Dicomposition.
#Methodology
BRISQUE - Blind reference image spatial quality evaluation and it is spatial because we are not converting image and using the original image. 
Brisque uses support vector regression model that is actually trained on bunch of images with known distortions such as noise, compression blurring etc as well as the same image without the distortions.



For Image Compression:-
SVD(Single value decomposition) SVD uses singular values which refactors the image and at the end of the process the image is represented with smaller set of values hence reducing the storage space of the image.
I have used Compression ratio for the model evaluation.

#Result
![new (1)](https://user-images.githubusercontent.com/64740121/177031116-5be048ce-f9bf-4e62-bafa-20b7279b255a.jpg)
Image compressed


![sample1](https://user-images.githubusercontent.com/64740121/177031127-90f92027-e86f-4168-9bdf-e2baba3ae179.jpg)
Original Image

and the BRISQUE score for the original image is 19.83849943878849
whereas for the Compressed image is 36.05348712342786
(Brisque score-0 for the best and 100 for worst)

Part1:
Code is matlab code: Question1.m. 
Just open the zip(Include the original Image and the code). And open the Question1.m then run it.  
![Cat](https://user-images.githubusercontent.com/65901340/99231919-36eb6280-282c-11eb-897c-f1779b86c873.png)

Show and store as 16x16 images the first ten principal components 
![1stPrincipalComponent](https://user-images.githubusercontent.com/65901340/99232484-ecb6b100-282c-11eb-8daa-f13fad331dbc.png)
![3rdPrincipalComponent](https://user-images.githubusercontent.com/65901340/99232501-f17b6500-282c-11eb-9822-1beb03b3ba01.png)
![5thPrincipalComponent](https://user-images.githubusercontent.com/65901340/99232516-f6d8af80-282c-11eb-93f5-01f08bb670be.png)
![7thPrincipalComponent](https://user-images.githubusercontent.com/65901340/99232524-f93b0980-282c-11eb-9182-720d16037616.png)
![10thPrincipalComponent](https://user-images.githubusercontent.com/65901340/99232529-fb04cd00-282c-11eb-9f6e-79a6108bc868.png)

How to select a better value for K?
In PCA, if k is too large, the data compression rate is not high. If k = the size of the original image, it is equivalent to using the original data; if k is too small, the approximate error of the data is too large.When determining the value of k, what we have to consider is the percentage of variance that can be preserved for different values of k. If = n, then our approximation of the data is perfect, that is to say, 100% of the variance of the data is retained, and all data changes are retained. If k=0, then only 0% of the change is retained.
The percentage of retained variance can be expressed by the sum of selected eigenvalues and the sum of all eigenvalues. I use code EigenValue./sum(EigenValue) to save Retention Rate.I choose K=150, the retention rate is 97.18%, the resultis very good, very close to orginal Image, and the compression rate is quite high.
![K=10_PCA_Image](https://user-images.githubusercontent.com/65901340/99231967-45397e80-282c-11eb-9a93-401bae98d09f.png)

![K=100_PCA_Image](https://user-images.githubusercontent.com/65901340/99231990-49659c00-282c-11eb-917f-e2c32d8fe080.png)

![K=150_PCA_Image](https://user-images.githubusercontent.com/65901340/99231890-305ceb00-282c-11eb-9bdc-cb60a2749f36.png)

Comment on the quality of the reconstructed images:
When K=10 the retention rate is 58.278% i can easily see the 16*16 blocks and the picture is rough, when K=100 the retention rate is 92.656%, the reconstruction image result is good and if you magnify the picture, you can see the blocks, and when i choose K=150 the retention is 97.18%, and the reconstruction image is very close to the original image. When K=200, the retention rate is 99.253%, it is nearly the same as the original, human can hardly find any difference beteween the reconstraction image and the original image.
![K=200_PCA_Image](https://user-images.githubusercontent.com/65901340/99232312-bbd67c00-282c-11eb-9ceb-abf08c2f2e55.png)

Part2:
Code is Question2Image_Stitching.py
Just open the zip(Include the original Image and the code). And open the Question1.m then run it.  The source image is Lodon_Left.jpg and Lodon_Right.jpg.
![London_Left](https://user-images.githubusercontent.com/65901340/99232169-8e89ce00-282c-11eb-82e1-568f24817d8e.jpg)

![London_Right](https://user-images.githubusercontent.com/65901340/99232181-90539180-282c-11eb-9081-c9377fac4355.jpg)

First use FLANNto analyzye and capturing an overlapping region, save them and mark them
![image](https://user-images.githubusercontent.com/65901340/99231427-909f5d00-282b-11eb-8032-13377efa6035.png)

Then reconstruct the image 
![image](https://user-images.githubusercontent.com/65901340/99232061-669a6a80-282c-11eb-8521-8cbc361f4da9.png)



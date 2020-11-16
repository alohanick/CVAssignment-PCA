
close all
clear all
clc
OrignalImage = imread('Cat.png');% Original image
K = 150;%Reconstructed against K principal components 
PatcheSize = 16;%16x16 non-overlapping patches

%Cut Image Part
OrignalImageArray = im2double(OrignalImage);%Read Image in Array Format,Three-Dimensional Matrice
[Row, Column] = size(OrignalImageArray);%Get size of the Image, Row and Column
Patch = zeros(PatcheSize*PatcheSize,(Row/PatcheSize)*(Column/PatcheSize));%Initialize Patch matrix
NumberOfPatches = 0;%Set a Variable to Record Number of Patches
for m = 1:PatcheSize:Row
    for n = 1:PatcheSize:Column
        NumberOfPatches = NumberOfPatches+1;
        Block = OrignalImageArray(m:m+PatcheSize-1,n:n+PatcheSize-1);
        Patch(:,NumberOfPatches) = Block(:);
    end
end

%PCA Part
NormalizedMatrix = Patch - ones(size(Patch,1),1)*mean(Patch);%Normalize the Patch Matrix 
CovarianceMatrix = cov(NormalizedMatrix');%Calculat the Covariance Matrix
[EigenVector,EigenValue] = eig(CovarianceMatrix);%Calculate the Eigenvalues and Eigenvectors
EigenValue = diag(EigenValue);%Take the eigenvalues of the diagonal
[EigenValue, T] = sort(EigenValue,'descend');%Arrange the eigenvalues in descending order
EigenVector = EigenVector(:,T);

%Clculate Retention Rate
RetentionRate = EigenValue./sum(EigenValue);
RetentionRateSum = sum(RetentionRate(1:	K));
%fprintf('选取%g个特征值的贡献率为：%g',K,ContributionRateSum);
fprintf('The %g Principal Components Retention Rate：%g',K,RetentionRateSum);

%Reconstructed Part   
NewVector = EigenVector(:,1:K);%Reconstructed Image,Take The First K Principal Components 
MappingMatrix = NewVector'* Patch;%The mapping matrix
RefactoringData = NewVector * MappingMatrix+ ones(size(NewVector, 1), 1) * mean(Patch);% Reconstructed the Image
NumberOfPatches = 0;
for m = 1:PatcheSize:Row
    for n = 1:PatcheSize:Column
        NumberOfPatches = NumberOfPatches + 1;
        RefactoringBlock = reshape(RefactoringData(:, NumberOfPatches), PatcheSize, PatcheSize);%Convert the Column vector to Blocks
        OutPutArray(m:m+PatcheSize-1, n:n+PatcheSize-1) = RefactoringBlock;%Output 
    end
end

%Show Reconstructed Image
RChannel = OutPutArray(:,1:Row);%Red Channel Array
GChannel = OutPutArray(:,Row+1:2*Row);%Blue Channel Array
BChannel = OutPutArray(:,2*Row+1:3*Row);%Green Channel Array
RGB = cat(3,RChannel,GChannel,BChannel);%Combine the R,G,B Channels to one RGB Channel to Output the Color Image 
figure(1),imshow(OrignalImageArray),title('OrignalImage') 
figure(2),imshow(RChannel),title(['R Channel,K=',num2str(K)])
figure(3),imshow(GChannel),title(['G Channel,K=',num2str(K)])
figure(4),imshow(BChannel),title(['B Channel,K=',num2str(K)])
figure(5),imshow(RGB),title(['Image processed by PCA,K=',num2str(K),' ,The Retention Rate is:',num2str(RetentionRateSum)]) 
%figure(5),imshow(RGB),title(['Image processed by PCA,the 10th principal components,The Retention Rate is:',num2str(RetentionRateSum)]) 
%imwrite(RGB,'Image processed by PCA.png')

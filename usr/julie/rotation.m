clear all;close all;clc;
%% Data Augmentaion: rotate 90,180,270, flip horizontally and vertically
for i = 1:70
    
    %Read img/mask
    i
    mask = imread(sprintf('mask%04d.JPG',i));
    I = imread(sprintf('img%04d.jpg',i));
    I = imgaussfilt(I,4);       %Add filtering
    
    %Rotation img/mask
    r90_mask = imrotate(mask,90);       %Rotate 90deg
    r180_mask = imrotate(mask,180);     %Rotate 180deg
    r270_mask = imrotate(mask,270);     %Rotate 270deg
    flipping_mask = flipdim(mask,2);    %Flip Horizontally
    
    r90_I = imrotate(I,90);
    r180_I = imrotate(I,180);
    r270_I = imrotate(I,270);
    flipping_I = flipdim(I,2);
    
    
    %Save img/mask j,k,l,s,n = img/mask name num
    %j = 70:140
    j = sprintf('%04i',i+70);
    filename_mask = ['mask',num2str(j),'.jpg'];
    imwrite(r90_mask,filename_mask);
    
    filename_I = ['img',num2str(j),'.jpg'];
    imwrite(r90_I,filename_I);
       
    
    %k = 141:210
    j = str2num(j);
    j
    k = sprintf('%04i',j+70);
    filename_mask = ['mask',num2str(k),'.jpg'];
    imwrite(r180_mask,filename_mask);
     
    filename_I = ['img',num2str(k),'.jpg'];
    imwrite(r180_I,filename_I);
    
    
    %l = 211:280
    k = str2num(k);
    k
    l = sprintf('%04i',k+70);
    
    filename_mask = ['mask',num2str(l),'.jpg'];
    imwrite(r270_mask,filename_mask);
    
    filename_I = ['img',num2str(l),'.jpg'];
    imwrite(r270_I,filename_I);
    
    
    %s = 281:350
    l = str2num(l);
    l
    s = sprintf('%04i',l+70);
    
    filename_mask = ['mask',num2str(s),'.jpg'];
    imwrite(flipping_mask,filename_mask);   
    
    filename_I = ['img',num2str(s),'.jpg'];
    imwrite(flipping_I,filename_I);
    
    
    %n = 351:420
    s = str2num(s);
    s
    n = sprintf('%04i',s+70);
    
    filename_mask = ['mask',num2str(n),'.jpg'];
    imwrite(flip(mask),filename_mask);

    filename_I = ['img',num2str(n),'.jpg'];
    imwrite(flip(I),filename_I);
    
    n = str2num(n);
    n
end

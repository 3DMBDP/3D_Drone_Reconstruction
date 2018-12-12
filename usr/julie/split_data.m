clc;close all;clear all;

%% Separate image into 4 sections 
for i = 1:800
    i
     I_img = imread(sprintf('img%04i.jpg',i));
     I_img = imresize(I_img,[512 512]);
     
     I_mask = imread(sprintf('mask%04i.jpg',i));
     I_mask = imresize(I_mask, [512 512]);

  %Fill holes
%     B = imfill(I,6);

    %Separate img/mask into 4
    [r_img c_img p_img]= size(I_img);
    A_img = I_img(1:r_img/2, 1:c_img/2, :);
    B_img = I_img(1:r_img/2, c_img/2 + 1:c_img, :);
    C_img = I_img(r_img/2 + 1:r_img, 1:c_img/2, :);
    D_img = I_img(r_img/2 + 1:r_img, c_img/2+1:c_img, :);

   [r_mask c_mask p_mask]= size(I_mask);
    A_mask = I_mask(1:r_mask/2, 1:c_mask/2, :);
    B_mask = I_mask(1:r_mask/2, c_mask/2+1:c_mask, :);
    C_mask = I_mask(r_mask/2+1:r_mask, 1:c_mask/2, :);
    D_mask = I_mask(r_mask/2+1:r_mask, c_mask/2+1:c_mask, :);
     
    %file location
    fileloc = 'C:\Users\JuliePark\Desktop\EC601\data\data';
    
    %Num for Img/mask name when i = 1, i1=1,i2=2,i3=3,i4=4 and i = 2,
    %i1=5,i2=6,i3=7,i4=8....
    i = i + 3*(i-1);
    
    i1 = i;     i2 = i+1;     i3 = i+2;     i4 = i+3;
    
    %Save each section as img#.jpg
    i1 = sprintf('%04i',i1);        
    filename_Aimg = ['img',num2str(i1),'.jpg'];  
    fullFileName_Aimg = fullfile(fileloc, filename_Aimg);
    imwrite(A_img,fullFileName_Aimg);
    
    i2 = sprintf('%04i',i2);    
    filename_Bimg = ['img',num2str(i2),'.jpg'];
    fullFileName_Bimg = fullfile(fileloc, filename_Bimg);
    imwrite(B_img,fullFileName_Bimg);
    
    i3 = sprintf('%04i',i3);    
    filename_Cimg = ['img',num2str(i3),'.jpg']; 
    fullFileName_Cimg = fullfile(fileloc, filename_Cimg);
    imwrite(C_img,fullFileName_Cimg);
    
    i4 = sprintf('%04i',i4);    
    filename_Dimg = ['img',num2str(i4),'.jpg'];
    fullFileName_Dimg = fullfile(fileloc, filename_Dimg);
    imwrite(D_img,fullFileName_Dimg);
        
    %Save each section as mask#.jpg    
    filename_Am = ['mask',i1,'.jpg'];      
    fullFileName_Am= fullfile(fileloc, filename_Am);
    imwrite(A_mask,fullFileName_Am);
    
    filename_Bm = ['mask',i2,'.jpg'];   
    fullFileName_Bm= fullfile(fileloc, filename_Bm);
    imwrite(B_mask,fullFileName_Bm);
    
    filename_Cm = ['mask',i3,'.jpg'];  
    fullFileName_Cm= fullfile(fileloc, filename_Cm);
    imwrite(C_mask,fullFileName_Cm);
    
    filename_Dm = ['mask',i4,'.jpg'];   
    fullFileName_Dm= fullfile(fileloc, filename_Dm);
    imwrite(D_mask,fullFileName_Dm);
    
    i1 = str2num(i1)
    i2 = str2num(i2)
    i3 = str2num(i3)
    i4 = str2num(i4)

end

%% Append data to the original data
for i = 1:800
    i
    I_img = imread(sprintf('img%04i.jpg',i));
    I_img = imresize(I_img,[512 512]);
      
    I_mask = imread(sprintf('mask%04i.jpg',i));
    I_mask = imresize(I_mask, [512 512]);

    
    i1 = sprintf('%04i',i+3200);
    filename_img = ['img',num2str(i1),'.jpg'];
    filename_mask = ['mask',num2str(i1),'.jpg'];
    
    imwrite(I_img,filename_img);
    imwrite(I_mask,filename_mask);
    
    i = sprintf('%04i',i);
    filename_imgd = ['img',num2str(i),'.jpg'];
    filename_maskd = ['mask',num2str(i),'.jpg'];
    
    delete(filename_imgd)
    delete(filename_maskd)
    
end

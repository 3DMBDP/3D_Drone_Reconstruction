clear all; close all; clc;

for i = 0225:0357
    
    %Folder = 'C:\Users\Julie Park\Desktop\sprint3';
    
    check = exist(sprintf('DJI_%04d.JPG',i));
    
    if check == 0
        continue;
    else
        i
        
        img = imread(sprintf('DJI_%04d.JPG',i));
        
        %img = imread(sprintf('DJI_0340.JPG'));
        extracted_img = imcrop(img,[700,800,3500,3500]);
        
        %imshow(extracted_img)
        filePath = fullfile('C:\Users\Julie Park\Desktop\sprint3\cropped', ['DJI_0' num2str(i) '_ext.JPG']);
        
        imwrite(extracted_img,filePath);
  
    end
    
    
    
    
       
    
% img = imread('seg1.png');
%img = imresize(img,[3000,4000]);
%figure(1);
%imshow(img);
 
    %figure(2);
    %imshow(img_f)
    %hold on;
    %rectangle('Position',[1100,920,3000,3500]);

    
    %figure(3);
    %imshow(extracted_img);
    
    
    

%sub_img = img - img_f;

%figure(3);
%imshow(sub_img);
end

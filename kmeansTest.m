clear; clc; clf; close all;

im = imread('1.png');
im = imresize(im,[1080,1920]);
% im = im(500:560,1290:1330,:); %3.png
% im = im(650:770,1200:1335,:);%2.png
im = im(300:390,730:875,:);%1.png

% iterative bilateral filter
patch = im;
patchVar = std2(patch)^2;
DoS = patchVar/20;
spat_sigma = 8;
for j = 1:20
    im = imbilatfilt(im,DoS, spat_sigma);
end

im = round(im ./ 10 ) * 10;

im_lab = rgb2lab(im);
im_lab_original = im_lab;

rgb_columns = reshape(im, [], 3);
[unique_colors, m, n] = unique(rgb_columns, 'rows');
color_counts = accumarray(n, 1);

[color_counts, id] = sort(color_counts);
unique_colors=unique_colors(id,:);

unique_colors_lab = rgb2lab(unique_colors);

for i = 1:size(color_counts)-10
   distance = Inf;
   best_ind = i;
   for j = i+1:size(color_counts)
      if sqrt(sum((unique_colors_lab(i,:) - unique_colors_lab(j,:)) .^ 2)) < distance
         distance =  sqrt(sum((unique_colors_lab(i,:) - unique_colors_lab(j,:)) .^ 2));
         best_ind = j;
      end
   end
%    for j = 1:i
%       if unique_colors_lab(i,:) == unique_colors_lab(j,:)
%           [row, col] = find(im_lab(:,:,1)==unique_colors_lab(j,1));
%           matrix1 = [row col];
%           [row, col] = find(im_lab(:,:,2)==unique_colors_lab(j,2));
%           matrix2 = [row col];
%           [row, col] = find(im_lab(:,:,3)==unique_colors_lab(j,3));
%           matrix3 = [row col];
%           
%           similar_color = intersect(intersect(matrix1, matrix2),matrix3);
%           
% %           im_lab(similar_color(1),similar_color(2),:) = unique_colors_lab(best_ind,:);
%           
%           unique_colors_lab(j,:) = unique_colors_lab(best_ind,:);
%           
%       end
%    end
   unique_colors_lab(i,:) = unique_colors_lab(best_ind,:);
end

unique_colors = lab2rgb(unique_colors_lab).*255;

new_unique_colors = [unique_colors(1,:) color_counts(1)];

for iter = 1:size(unique_colors)
    loops = size(new_unique_colors,1);
    for i = 1:loops
       if new_unique_colors(i,1:3) == unique_colors(iter,:)
           new_unique_colors(i,4) = new_unique_colors(i,4) + color_counts(iter);
           break
       end
       if i == loops
          new_unique_colors = [new_unique_colors; unique_colors(iter,:) color_counts(iter)];
       end
    end
    
end

im = uint8(lab2rgb(im_lab).*255);

image(im);
unique_colors = new_unique_colors(:,1:3);
color_counts = new_unique_colors(:,4);

[color_counts, id] = sort(color_counts);
unique_colors=unique_colors(id,:);

ind1 = size(color_counts,1);
ind2 = size(color_counts,1)-1;
ind3 = size(color_counts,1)-2;
ind4 = size(color_counts,1)-3;
ind5 = size(color_counts,1)-4;
ind6 = size(color_counts,1)-5;
ind7 = size(color_counts,1)-6;
ind8 = size(color_counts,1)-7;
ind9 = size(color_counts,1)-8;
ind10 = size(color_counts,1)-9;

% [max1, ind1] = max(color_counts);
% color_counts(ind1)      = -Inf;
% [max2, ind2] = max(color_counts);
% color_counts(ind2)      = -Inf;
% [max3, ind3] = max(color_counts);
% color_counts(ind3)      = -Inf;
% 
% color_counts(color_counts == -Inf) = Inf;

rgbC1 = unique_colors(ind1, 1:3);
rgbC2 = unique_colors(ind2, 1:3);
rgbC3 = unique_colors(ind3, 1:3);
rgbC4 = unique_colors(ind4, 1:3);
rgbC5 = unique_colors(ind5, 1:3);
rgbC6 = unique_colors(ind6, 1:3);
rgbC7 = unique_colors(ind7, 1:3);
rgbC8 = unique_colors(ind8, 1:3);
rgbC9 = unique_colors(ind9, 1:3);
rgbC10 = unique_colors(ind10, 1:3);

color1 = [-1 -1 -1];
color2 = [-1 -1 -1];
color3 = [-1 -1 -1];

color1 = rgbC1;

distance = 30;
j = 2;
while sqrt(sum((color1 - unique_colors_lab(j,:)) .^ 2)) < distance
    j = j +1;
end
color2 = unique_colors_lab(j,:);
j = j + 1;
while sqrt(sum((color1 - unique_colors_lab(j,:)) .^ 2)) < distance && sqrt(sum((color2 - unique_colors_lab(j,:)) .^ 2)) < distance
    j = j +1;
end
color3 = unique_colors_lab(j,:);
% plots colors
x = [0 1 1 0] ; y = [0 0 1 1] ;
figure
subplot(2,5,1);
fill(x,y,double(rgbC1)/255)
subplot(2,5,2);
fill(x,y,double(rgbC2)/255)
subplot(2,5,3);
fill(x,y,double(rgbC3)/255);
subplot(2,5,4);
fill(x,y,double(rgbC4)/255);
subplot(2,5,5);
fill(x,y,double(rgbC5)/255);
subplot(2,5,6);
fill(x,y,double(rgbC6)/255)
subplot(2,5,7);
fill(x,y,double(rgbC7)/255)
subplot(2,5,8);
fill(x,y,double(rgbC8)/255);
subplot(2,5,9);
fill(x,y,double(rgbC9)/255);
subplot(2,5,10);
fill(x,y,double(rgbC10)/255);


% 
% redOrig = reshape(im(:,:,1),size(im,1)*size(im,2),1); % Red channel
% greenOrig = reshape(im(:,:,2),size(im,1)*size(im,2),1); % Green channel
% blueOrig = reshape(im(:,:,3),size(im,1)*size(im,2),1); % Blue channel
% 
% rgbOrig = [double(redOrig) double(greenOrig) double(blueOrig)];   
% 
% K = 3; % number of clusters
% iter = 0;
% %C = zeros(K,3);
% %G = zeros(size(rgbOrig,1),1);
% 
% while true
%     [G,C] = kmeans(rgbOrig, K, 'distance', 'sqEuclidean', 'start', 'sample');
%     iter = iter + 1;
%     if sum(pdist(C,'euclidean')>20)==3 || iter > 100
%         rgbC1 = C(1,:);
%         rgbC2 = C(2,:);
%         rgbC3 = C(3,:);
% 
%         % plots the colors of the centroids
%         x = [0 1 1 0] ; y = [0 0 1 1] ;
%         figure
%         subplot(1,3,1);
%         fill(x,y,rgbC1/255)
%         subplot(1,3,2);
%         fill(x,y,rgbC2/255)
%         subplot(1,3,3);
%         fill(x,y,rgbC3/255);
% 
%         % plots the kmeans scatter plot
%         clr = lines(K);
%         figure, hold on
%         scatter3(rgbOrig(:,1), rgbOrig(:,2), rgbOrig(:,3), 36, clr(G,:), 'Marker','.')
%         scatter3(C(:,1), C(:,2), C(:,3), 100, clr, 'Marker','o', 'LineWidth',3)
%         hold off
%         view(3), axis vis3d, box on, rotate3d on
%         xlabel('x'), ylabel('y'), zlabel('z')
%         break
%     end
% end


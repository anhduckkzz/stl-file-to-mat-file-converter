% Orthogonal matrices and 3d rotation

%% 3D fawn
clear;

% Load vertices and edges from MAT files
load('vertice.mat', 'vertice');
load('edge.mat', 'edge');

[mVert, nVert] = size(vertice);
[mFace, nFace] = size(edge);

figure;
axis equal;
hold on;
for j = 1:mFace
    line([vertice(edge(j,1),1), vertice(edge(j,2),1)], ...
         [vertice(edge(j,1),2), vertice(edge(j,2),2)], ...
         [vertice(edge(j,1),3), vertice(edge(j,2),3)], 'Color', 'blue');
    line([vertice(edge(j,1),1), vertice(edge(j,3),1)], ...
         [vertice(edge(j,1),2), vertice(edge(j,3),2)], ...
         [vertice(edge(j,1),3), vertice(edge(j,3),3)], 'Color', 'blue');
    line([vertice(edge(j,2),1), vertice(edge(j,3),1)], ...
         [vertice(edge(j,2),2), vertice(edge(j,3),2)], ...
         [vertice(edge(j,2),3), vertice(edge(j,3),3)], 'Color', 'blue');    
end
hold off;

figure;
axis equal;
hold on;

theta1 = pi/3;
theta2 = pi/4;
theta3 = pi/2;

rotmat = rotation(theta1, theta2, theta3);

VertRot = vertice * rotmat;

for j = 1:mFace
    line([VertRot(edge(j,1),1), VertRot(edge(j,2),1)], ...
         [VertRot(edge(j,1),2), VertRot(edge(j,2),2)], ...
         [VertRot(edge(j,1),3), VertRot(edge(j,2),3)], 'Color', 'blue');
    line([VertRot(edge(j,1),1), VertRot(edge(j,3),1)], ...
         [VertRot(edge(j,1),2), VertRot(edge(j,3),2)], ...
         [VertRot(edge(j,1),3), VertRot(edge(j,3),3)], 'Color', 'blue');
    line([VertRot(edge(j,2),1), VertRot(edge(j,3),1)], ...
         [VertRot(edge(j,2),2), VertRot(edge(j,3),2)], ...
         [VertRot(edge(j,2),3), VertRot(edge(j,3),3)], 'Color', 'blue');
end

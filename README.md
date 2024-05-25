**STL file to MAT file converter**

*General*:
This python code will generate for you 4 file: vertice.mat, vertice.txt, edge.mat, edge.txt
vertice.mat and edge.mat are the 2 files you will use to draw your 3D shape, the other two txt files just use to check what is written in the file.

This will help you to convert a 3D picture and reconstructor that 3D shape on MATLAB using data is vertices and edges;

Step-by-step using this code:

**1.** Open the STL file to check the number of TRIANGLE of the 3D shape in the Stats & Shading section ( look at the pics)

 ![image](https://github.com/anhduckkzz/stl-file-to-mat-file-converter/assets/158149029/52ac3799-f96a-45f9-965b-b5a5d2ad57a5)
![image](https://github.com/anhduckkzz/stl-file-to-mat-file-converter/assets/158149029/b2acfa58-f3f5-406a-8b5b-2d0f1aa30aa2)


**2.** Change the convert code with THE NUMBER OF TRIANGLES that you have just checked ( the python file):

![image](https://github.com/anhduckkzz/stl-file-to-mat-file-converter/assets/158149029/59a29e79-0e79-4b53-a5bf-e44ec46125ac)

At the line 75: edge_array = edge_array.reshape(29996, 3), you will see the number of triangles(29996), customs that number with your "number of triangles" you have just checked, for example:
the bunny model picture has 292 triangles, as shown in the STL file, so I will change the code from: edge_array = edge_array.reshape(29996, 3) -> edge_array = edge_array.reshape(292, 3).
Note: Do not touch anything else,even the number 3 next to the number you have just change.

**3.** After you have already had two data files, use the code "code_to_run_custom_data.m" and open the MATLAB to run, remember to import the 2 files you have just got.

Note: the code "run_custom_data_one_color" is exactly the same with the above MATLAB code, just change the color of the 3D shape into one particular color - blue(you can change another color) :))
If the code cannot run using online version, use offline version.

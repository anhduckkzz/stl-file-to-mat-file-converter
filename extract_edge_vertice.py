import numpy as np
import struct
import stl
from stl import mesh
from scipy.io import savemat

def parse_stl(filename):
    # Load the STL file
    mesh_data = mesh.Mesh.from_file(filename)

    # Extract vertices and faces
    vertices = mesh_data.vectors.reshape((-1, 3))
    faces = np.arange(len(vertices)).reshape((-1, 3))

    return vertices, faces

def write_to_txt(vertices, filename):
    with open(filename, 'w') as f:
        for vertex in vertices:
            # Format each vertex to have 4 decimal places
            f.write(f"{vertex[0]:.4f} {vertex[1]:.4f} {vertex[2]:.4f}\n")

# Read STL file
filename = 'Diplodocus.stl'

# Parse STL and get vertices
vertices, _ = parse_stl(filename)

# Save vertices to text file
write_to_txt(vertices, 'vertice.txt')

# Read STL file
with open(filename, 'rb') as f:
    # Skip header
    f.seek(80)
    
    # Read number of triangles
    num_triangles = struct.unpack('<I', f.read(4))[0]

    # Initialize array to store triangles
    triangles = np.zeros((num_triangles, 3), dtype=np.uint32)

    for i in range(num_triangles):
        # Skip vertices
        f.seek(12, 1)  # Move 12 bytes forward from the current position
        
        # Read attribute
        attribute = struct.unpack('<H', f.read(2))[0]
        
        # Store triangle indices
        triangles[i] = (i * 3 + 1, i * 3 + 2, i * 3 + 3)

# Save triangle indices to text file
np.savetxt('edge.txt', triangles, fmt='%d')

# Read vertices from the txt file
edge = []
vertice = []
# read the edge.txt file
with open('edge.txt', 'r') as f:
    for line in f:
        # Split the line into coordinates and convert them to floats
        edge_parse = tuple(map(float, line.strip().split()))
        edge.append(edge_parse)

# read the vertices.txt file
with open('vertice.txt', 'r') as f:
    for line in f:
        # Split the line into coordinates and convert them to floats
        x, y, z = map(float, line.strip().split())
        vertice.append([x, y, z])
# Convert the list of vertices to a numpy array and reshape it to desired size

edge_array = np.array(edge)
edge_array = edge_array.reshape(29996, 3)

# Convert the list of vertices to a numpy array
vertice_array = np.array(vertice)

# Save vertices to a binary MAT-file
savemat('edge.mat', {'edge': edge_array})
savemat('vertice.mat', {'vertice': vertice_array})

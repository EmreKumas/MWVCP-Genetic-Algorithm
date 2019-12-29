# GLOBAL VARIABLES
vertex_count = None
edge_count = None
vertex_weights = []
adjacency_matrix = [[]]


# noinspection PyUnusedLocal
def read_file(file_name):

    # Global variables...
    global vertex_count, edge_count, vertex_weights, adjacency_matrix
    file = open(file_name, 'r')

    # Read the file till the end...
    while True:
        # Read the line and remove the newline character at the end
        line = file.readline().rstrip('\n\r')
        if not line:
            # Means we reached to the end of file...
            break

        if vertex_count is None:
            # Then this is the line for indicating the number of vertices...
            vertex_count = int(line)

            # After we get the vertex count, we initialize adjacency matrix with zeros...
            adjacency_matrix = [[0 for i in range(vertex_count)] for i in range(vertex_count)]

        elif edge_count is None:
            # Then this is the line for indicating the number of edges...
            edge_count = int(float(line))
        elif len(vertex_weights) == 0:
            # These are the lines indicating vertex weights...
            for i in range(vertex_count):
                # Get only the second part of the string...
                _, _, line = line.partition(' ')
                # Convert comma separated values into dot separated...
                line = line.replace(',', '.')
                # Add the value into vertex weights list as float type...
                vertex_weights.append(float(line))

                # We will read the next line, if this is not the last vertex's weight...
                if i + 1 != vertex_count:
                    line = file.readline().rstrip('\n\r')
        else:
            # These are the lines indicating edges between vertices...
            line = line.split()
            # The first element of line is row and second element of line is column...
            adjacency_matrix[int(line[0])][int(line[1])] = 1

    # Close the file...
    file.close()


if __name__ == '__main__':

    FILE_NAME = 'example_graph_1.txt'
    read_file(FILE_NAME)

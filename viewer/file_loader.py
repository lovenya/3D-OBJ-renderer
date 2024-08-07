# file_loader.py

import ifcopenshell


class FileLoader:
    @staticmethod
    def load_obj(file_path):
        if not file_path.endswith(".obj"):
            raise ValueError("Unsupported file format. Please upload an OBJ file.")

        with open(file_path, "r") as file:
            data = file.read()
        return data

    @staticmethod
    def parse_obj(data):
        # Basic OBJ parsing logic; you can replace this with a proper OBJ parser library if needed
        vertices = []
        faces = []

        for line in data.splitlines():
            if line.startswith("v "):
                vertices.append([float(x) for x in line.strip().split()[1:4]])
            elif line.startswith("f "):
                faces.append([int(x.split("/")[0]) for x in line.strip().split()[1:4]])

        return vertices, faces

import os

def find_files(suffix, path):
    paths = []
    if (os.path.isdir(path)):
        contents = os.listdir(path)

        if len(contents) > 0:
            for obj in contents:
                # Files/Folders in dir have a path relative to dir
                # We need full path
                full_path = os.path.join(path, obj)

                # If obj is a folder, then recursively search through it
                if (os.path.isdir(full_path)):
                    paths.extend(find_files(suffix, full_path))
                # If obj is not a folder and therefore a file, check it ends with the suffix
                elif (full_path.endswith(suffix)):
                    paths.append(full_path)
    elif (path.endswith(suffix)):
        paths.append(path)

    return paths
print(find_files('.c', './testdir/'))
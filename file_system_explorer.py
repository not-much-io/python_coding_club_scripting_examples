from glob import glob
import os


def file_with_extension_in_directory(directory_path, extension):
    search_query = directory_path + extension
    return glob(search_query)


def find_in_tree(root_dir, extension):
    found_files = []

    for dirName, subdirList, fileList in os.walk(root_dir):
        found_files += file_with_extension_in_directory(dirName, extension)

    return found_files


if __name__ == "__main__":

    all_mp3s = find_in_tree("/", "/*.mp3")

    for mp3 in all_mp3s:
        print(mp3)

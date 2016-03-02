from glob import glob
import os


def files_with_extension(dir_path, ext):
    search_query = dir_path + ext
    return glob(search_query)


def find_in_tree(root_dir, ext):
    found_files = []

    for dirName, _, _ in os.walk(root_dir):
        found_files += files_with_extension(dirName, ext)

    return found_files


if __name__ == "__main__":
    all_mp3s = find_in_tree("/", "/*.mp3")
    for mp3 in all_mp3s:
        print(mp3)

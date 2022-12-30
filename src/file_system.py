from os import scandir
import shutil


def scan_tree(path, search_term):
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            if entry.name == search_term:
                yield entry
            else:
                yield from scan_tree(entry.path, search_term)  # see below for Python 2.x


def run_search(path, search_term):
    matches = []
    for entry in scan_tree(path, search_term):
        matches.append({'path_obj': entry})
    return matches


def rm_folders(folders_to_rm):
    for path_dict in folders_to_rm:
        if path_dict['to_remove'] == 'True':
            shutil.rmtree(path_dict['path_obj'].path)

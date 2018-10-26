import os


def check_dir(dirname):
    """
    Check the input dirname whether exists
    If exist: do nothing
    If not exist: make the dir path all exists
    :param dirname: the check dir path
    :return: None

    """
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def split_file(path):
    """
    Get the file name and extension for the given path
    :param path: The path of a file
    :return: the file name without extension and the file extension

    """
    if os.path.exists(path):
        if os.path.isfile(path):
            data = os.path.split(path)
            datas = os.path.splitext(data[-1])
            return datas
        else:
            raise Exception('The path is not a file path!')
    else:
        raise Exception('The path doesn\'t exist')


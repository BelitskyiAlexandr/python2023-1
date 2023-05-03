import os

def mk_pkg(path, root_path='/home/alexandr/University/python2023-1/lab3/5'):
    #full path
    full_path = os.path.join(root_path, *path.split('/'))
    print(full_path)
    # check exist dirs
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    
    # init in dirs
    for dirpath, _, _ in os.walk(full_path):
        init_file = os.path.join(dirpath, '__init__.py')
        if not os.path.exists(init_file):
            open(init_file, 'a').close()




mk_pkg('pkg_1/pkg_2')
mk_pkg('pkg_1/pkg_3/pkg_4')

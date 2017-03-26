import os
import shutil

def create_new_folder(path ,folder_name):
    flag1 = os.path.exists(path)
    flag2 = os.path.isdir(path)
    if flag1 and flag2:
        print("path is valid and is a folder!")
    else:
        print("path is invalid and not a folder!")
        exit(-1)
    current_directory = os.getcwd()
    print(current_directory)
    os.chdir(path)
    print("switched the path: %s" %(path))
    os.mkdir(folder_name)

def copy_folder_files_to_current_folder(src_path, dst_path):
    folder_details = os.listdir(src_path)
    print(folder_details)
    for detail in folder_details:
        if os.path.isfile(os.path.join(src_path ,detail)):
            try:
                shutil.copy(os.path.join(src_path ,detail), dst_path)
            except IOError as err:
                print(err)
        else:
            pass
    print("copy all src_files to %s" %(dst_path))

def git_add_files(path): # path is file_path or folder_path
    flag1 = os.path.exists(path)
    flag2 = os.path.isdir(path)
    flag3 = os.path.isfile(path)
    if flag1 and flag2: # path is a folder_path
        print("path is valid and is a folder!")
        folder_details = os.listdir(path)
        print(folder_details)
        for detail in folder_details:
            if os.path.isfile(os.path.join(path ,detail)):
                try:
                    log = os.system("git add %s" %(detail))
                    print(log)
                except Exception as err:
                    print(err)
            else:
                pass
    elif flag1 and flag3: # path is a file_path
        print("path is valid and is a file!")
        file_name = os.path.split(path)[1]
        try:
            log = os.system("git add %s" %(file_name))
            print(log)
        except Exception as err:
                print(err)
    else:
        print("path is invalid and not a folder!")
        exit(-1)

def one_repository_commit_to_current_repository_branch(src_repository_path ,dst_repository_path ,dst_branch_name):
    flag1 = os.path.exists(dst_repository_path)
    flag2 = os.path.isdir(dst_repository_path)
    if flag1 and flag2: # path is a folder_path
        os.chdir(dst_repository_path)
    else:
        exit(-1)
    os.system("git checkout %s" %(dst_branch_name))
    os.system("git remote add other %s" %(src_repository_path))
    os.system("git fetch other")
    os.system("git checkout -b temp other/master")
    log = os.system("git merge temp --allow-unrelated-histories")
    print(log)
    list_file_update("HEAD" ,"HEAD^")
    os.system("git checkout master")
    os.system("git branch -D temp")

def list_file_update(commit_id_1 , commit_id_2):
    log = os.system("git diff %s %s" %(commit_id_1 ,commit_id_2))
    print(log)

if __name__ == "__main__":
    code1_path = r"C:\Users\Administrator\Desktop\my_git_homework\code1"
    code2_path = r"C:\Users\Administrator\Desktop\my_git_homework\code2"
    code3_path = r"C:\Users\Administrator\Desktop\my_git_homework\code3"
    path_1 = r"C:\Users\Administrator\Desktop\my_git_homework"
    create_new_folder(path_1 ,"version")
    path_2 = r"C:\Users\Administrator\Desktop\my_git_homework\version"
    os.chdir(path_2)
    os.system("git init")
    copy_folder_files_to_current_folder(code1_path ,path_2)
    git_add_files(path_2)
    os.system('git commit -m "Initialize the commit"')
    os.system("git branch version_branch_A")
    os.system("git branch version_branch_B")
    os.system("git branch version_branch_C")
    create_new_folder(path_1 ,"LTE")
    path_1 = r"C:\Users\Administrator\Desktop\my_git_homework\LTE"
    create_new_folder(path_1 ,"pub")
    path_2 = r"C:\Users\Administrator\Desktop\my_git_homework\LTE\pub"
    os.chdir(path_2)
    os.system("git init")
    copy_folder_files_to_current_folder(code2_path ,path_2)
    git_add_files(path_2)
    os.system('git commit -m "Initialize the commit"')
    os.system("git branch pub_branch_A")
    os.system("git branch pub_branch_B")
    os.system("git branch pub_branch_C")
    create_new_folder(path_1 ,"sdr")
    path_2 = r"C:\Users\Administrator\Desktop\my_git_homework\LTE\sdr"
    os.chdir(path_2)
    os.system("git init")
    copy_folder_files_to_current_folder(code3_path ,path_2)
    git_add_files(path_2)
    os.system('git commit -m "Initialize the commit"')
    os.system("git branch sdr_branch_A")
    os.system("git branch sdr_branch_B")
    os.system("git branch sdr_branch_C")

    src_repository_path = r"C:\Users\Administrator\Desktop\my_git_homework\version"
    dst_repository_path = r"C:\Users\Administrator\Desktop\my_git_homework\LTE\pub"
    dst_branch_name = "pub_branch_A"
    one_repository_commit_to_current_repository_branch(src_repository_path ,dst_repository_path ,dst_branch_name)
#    list_file_update("HEAD" , "HEAD^")



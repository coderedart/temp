import platform
import os

print("platform: ", platform.system())
print("printing env vars:")
for key, value in os.environ.items():
    print("    ", key, value)

if platform.system() == "Windows" :
    llvm_path = "C:\\Program Files\\LLVM"
    if os.path.isdir(llvm_path):
        print(llvm_path, " exists")
    else:
        print(llvm_path, " doesn't exist")
    os.system("choco install ninja")
    os.system("ninja --version")

os.system("clang++ --version")



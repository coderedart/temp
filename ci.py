import platform
import os

print("platform: ", platform.system())
print("printing env vars:")
for key, value in sorted(os.environ.items()):
    print("    ", key, value)
if os.environ['RUNNER_OS'] == 'Linux':
    file_list = os.listdir(r"/usr/local/lib/android/sdk/")
    print(file_list)


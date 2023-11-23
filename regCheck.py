import platform, distro
#Use .pyw extension for no terminal when running

#Steps for Program:
'''
    1. Determine OS
    2. Determine if new Agent or Existing
    3. Determine ingestion settings / location
    4. Create persistence
    
'''
# Determine OS and return String
def get_operating_system():
    system_info = platform.system()
    if system_info == "Windows":
        return "Windows"
    elif system_info == "Linux":
        distribution = distro.name()
        if "Ubuntu" in distribution:
            return "Ubuntu"
        else:
            return "Linux (other)"
    elif system_info == "Darwin":
        return "macOS"
    else:
        return "Unknown"

if __name__ == "__main__":
    operating_system = get_operating_system()
    print(operating_system)

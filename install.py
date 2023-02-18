# Importing Libraries
import getpass
import os
import platform

# Variables
home_directory = f"/home/{getpass.getuser()}"
ubuntu_packages = [
    "tmux",
    "python3-pip",
    "lightdm",
    "curl",
    "wget",
    "zsh",
    "lolcat",
    "dconf-editor",
    "software-properties-common",
    "build-essential",
    "gnome-tweaks",
    "gnome-shell-extensions",
    "code",
]
kali_packages = [
    "zsh",
    "lolcat",
    "tmux",
    "python3-pip",
    "curl",
    "dnsrecon",
    "enum4linux",
    "feroxbuster",
    "gobuster",
    "nbtscan",
    "onesixtyone",
    "oscanner",
    "smbclient",
    "smbmap",
    "snmpwalk",
    "sslscan",
    "svwar",
    "tnscmd10g",
    "whatweb",
    "wkhtmltopdf",
    "redis-tools",
    "impacket-scripts",
    "code",
    "python3-venv",
]
zsh_config_path = f"{home_directory}/.zshrc"
banner = "lolcat ~/banner"
current_os = platform.uname().node


# Configuring Shell, Fonts and Wallpaper
def configure():
    print("Installing Oh-my-Zsh")
    os.system(
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended'
    )
    os.system("cp banner ~")
    with open(zsh_config_path) as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    print(content)
    if banner in content:
        print(banner)
        file.close()
    else:
        with open(zsh_config_path, "a") as f:
            f.write(banner + "\n" + f"source {home_directory}/zsh/aliases.zsh")
            # f.write()
        f.close()
    os.system("cp ./tmux/.tmux.conf ~")
    print(".....Installing Fonts......")
    os.system('sudo cp -r ./fonts/"Anonymous Pro" /usr/share/fonts/truetype')
    os.system('sudo cp -r ./fonts/"Fira Code" /usr/share/fonts/truetype')
    os.system("sudo cp -r ./fonts/Monaco /usr/share/fonts/truetype")
    print("...Fonts are installed.....")
    os.system("cp -r ./wallpapers ~/Pictures/")
    os.system("cp -r ./zsh ~")
    os.system(f"source {zsh_config_path}")


# Updating and Upgrading the system
def update():
    os.system("sudo apt-get update -y && sudo apt-get full-upgrade -y")
    os.system("sudo apt autoremove -y")


# Adding Code to sources-list to install via terminal
def textEditor():
    os.system(
        "wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg"
    )
    os.system(
        "sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/"
    )
    os.system(
        "sudo sh -c 'echo \"deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main\" > /etc/apt/sources.list.d/vscode.list'"
    )
    os.system("rm -f packages.microsoft.gpg")


# Installing packages for Ubuntu
def configure_ubuntu():
    textEditor()
    update()
    for package in ubuntu_packages:
        os.system(f'echo "Installing {package}"')
        os.system(f"sudo apt-get install {package} -y -qq")
    configure()
    os.system("code .")


# Installing packages for Kali Linux
def configure_kali():
    textEditor()
    update()
    for package in kali_packages:
        os.system(f'echo "Installing {package}"')
        os.system(f"sudo apt-get install {package} -y -qq")
    configure()
    os.system("code .")
    os.system(
        "sudo python3 -m pip install git+https://github.com/Tib3rius/AutoRecon.git"
    )
    boxes = input("Do you want to create a folder for Practicing Boxes?(y/n) : ")
    if boxes == "y" and not os.path.exists(f"{home_directory}/Desktop/Boxes"):
        os.mkdir(f"{home_directory}/Desktop/Boxes")
        os.mkdir(f"{home_directory}/Desktop/Boxes/HTB")
        os.mkdir(f"{home_directory}/Desktop/Boxes/HTB/vpns")
        os.mkdir(f"{home_directory}/Desktop/Boxes/THM")
        os.mkdir(f"{home_directory}/Desktop/Boxes/THM/vpns")
    else:
        print("Boxes folder already exists!!!")


# Install script
def install(operating_system):
    if current_os == "ubuntu":
        configure_ubuntu()
    elif current_os == "kali":
        configure_kali()


install(current_os)

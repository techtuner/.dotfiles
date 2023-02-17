# Python script to configure Ubuntu, Kali and Windows.... WORK IN PROGRESS
import os
import subprocess
import sys
import io
import getpass
import platform

print(platform.uname().node)

# operating_system = sys.argv[1].lower()
home_directory = f'/home/{getpass.getuser()}'
ubuntu_packages = ['tmux','python3-pip','lightdm','curl','wget','zsh','lolcat','dconf-editor','software-properties-common','build-essential','gnome-tweaks','gnome-shell-extensions']
kali_packages = ['lolcat','python3-pip','curl','dnsrecon','enum4linux','feroxbuster','gobuster','nbtscan','onesixtyone','oscanner','smbclient','smbmap','snmpwalk','sslscan','svwar','tnscmd10g','whatweb','wkhtmltopdf','redis-tools','impacket-scripts']
zsh_config_path = f'{home_directory}/.zshrc'
banner = 'lolcat ~/banner'
current_os = platform.uname().node
def configure():

	print("Installing Oh-my-Zsh")
	os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
	os.system('cp banner ~')
	with open(zsh_config_path) as file:
		content = file.readlines()
	content = [x.strip() for x in content]
	print(content)
	if banner in content:
		print(banner)
		file.close()
	else:
		with open(zsh_config_path,'a') as f:
			f.write(banner + '\n' +f'source {home_directory}/zsh/aliases.zsh')
			# f.write()
		f.close()		
	os.system('cp ./tmux/.tmux.conf ~')
	print('.....Installing Fonts......')
	os.system('sudo cp -r ./fonts/"Anonymous Pro" /usr/share/fonts/truetype')
	os.system('sudo cp -r ./fonts/"Fira Code" /usr/share/fonts/truetype')
	print('...Fonts are installed.....')
	os.system('cp -r ./wallpapers ~/Pictures/')
	os.system('cp -r ./zsh ~')
	os.system(f'source {zsh_config_path}')


def update():
	os.system('sudo apt-get update -y && sudo apt-get full-upgrade -y')
	os.system('sudo apt autoremove -y')

def configure_ubuntu():
	update()
	for package in ubuntu_packages:
		os.system(f'echo "Installing {package}"')
		os.system(f'sudo apt-get install {package} -y -qq')
	configure()


def configure_kali():
	update()
	for package in ubuntu_packages:
		os.system(f'echo "Installing {package}"')
		os.system(f'sudo apt-get install {package} -y -qq')
	configure()

def install(operating_system):

	if current_os == 'ubuntu':
		configure_ubuntu()
	elif current_os == 'kali':
		configure_kali()
	elif operating_system == 'windows' or sys.argv[1]=="":
		configure_windows()

install(current_os)

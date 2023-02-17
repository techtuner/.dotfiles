# Aliases
alias src="source ~/.zshrc"
alias python="python3"
alias pip="pip3"
alias vim="nvim"
alias vi="nvim"
alias lg="lazygit" # Works only inside a git folder or can be used to initialize a git folder
alias e="exit"
alias neofetch="neofetch --source /home/techtuner/.config/neofetch/cicada"
alias ll="exa -l -g --icons --git"
alias lt="exa -l --tree --icons --git-ignore"
alias dots="cd ~/Downloads/dotfiles && ls"
alias wallpapers=" gio open ~/Pictures/wallpapers" 
# Git Aliases

alias ga="git add"
alias gaa="git add ."
alias gs="git status"
alias gpo="git push origin main"
alias gp="git push origin"
alias gcm="git commit -m"


# Scripts
alias ide="~/ide.sh" # Used to split tmux into vscode like
alias notes="cd ~/scripts/ && chmod +x notes.sh && ./notes.sh && source notes.sh"
alias projects="cd ~/scripts/ && chmod +x projects.sh && ./projects.sh && source projects.sh"

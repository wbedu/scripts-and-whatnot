# Prompt settings
export PS1="\[\033[38;5;11m\]\u\[\033[38;5;15m\]@\[\033[38;5;6m\]\h\[\033[38;5;15m\]:\[\033[38;5;10m\]\w\[\033[38;5;15m\]\$ \[\033[0m\]"

# Aliases
alias ls='ls --color=auto'
alias ll='ls -alF'
alias grep='grep --color=auto'

# Colored man pages
export LESS_TERMCAP_mb=$'\E[01;31m'
export LESS_TERMCAP_md=$'\E[01;31m'
export LESS_TERMCAP_me=$'\E[0m'
export LESS_TERMCAP_se=$'\E[0m'
export LESS_TERMCAP_so=$'\E[01;44;33m'
export LESS_TERMCAP_ue=$'\E[0m'
export LESS_TERMCAP_us=$'\E[01;32m'

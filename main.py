import apps

import os
import argparse

symlinks = {
    "zsh/zshrc.zsh": ".zshrc",
    "git/gitconfig": ".gitconfig",
    "git/gitignore_global": ".gitignore_global",
    "karabiner/karabiner.edn": ".config/karabiner.edn",
    "Library/Application Support/Code - Insiders/User/keybindings.json": "vscode/keybindings.json",
    ".ideavimrc": "idea/.vimrc",
    ".vimrc": "vim/.vimrc"
}


def create_symlinks():
    home_dir = os.getenv("HOME")
    dot_dir = os.path.join(home_dir, "dotfiles")

    for src_fname, dst_fname in symlinks.items():
        src = os.path.join(dot_dir, src_fname)
        dst = os.path.join(home_dir, dst_fname)
        os.symlink(src, dst)
        print("created symlink\n\tfrom:%s\n\tto:%s" % (src, dst))


def install_vscode_extensions():
    for name in apps.vscode_extension:
        os.system("code --install-extension %s" % name)


def install_brew():
    os.system(
        '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')


def install_brew_apps():
    for name in apps.brew:
        try:
            os.system("brew list %s" % name)
            print("%s already installed" % name)
        except Exception:
            os.system("brew install %s" % name)


def open_app_urls():
    for url in apps.urls:
        os.system("open %s" % url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("mac config setup")

    # (VSCode and Karabiner need to be installed)
    parser.add_argument("--apps", help="opens urls for apps that need manual installation",
                        aciton="store_true")
    parser.add_argument("--symlinks", help="symlinks for configs", 
                        action="store_true")
    parser.add_argument("--brew", help="install brew", 
                        action="store_true")
    parser.add_argument("--brew-apps", help="install brew apps",
                        action="store_true")
    parser.add_argument("--vscode-ext", help="install vscode extension",
                        action="store_true")
    args = parser.parse_args()
    
    if args.apps:
        open_app_urls()
        res = input("have apps been installed: yes(Y), no(N)")
        if res.lower() not in ['yes', 'y']:
            exit()
    
    if args.symlinks:
        create_symlinks()
        
    if args.brew:
        install_brew()
    
    if args.brew_apps:
        install_brew_apps()
        
    if args.vscode_ext():
        install_vscode_extensions()

import os
import vscode.extensions
import brew.apps
import apps

symlinks = {
    "zsh/zshrc.zsh" : ".zshrc",
    "git/gitconfig" : ".gitconfig",
    "git/gitignore_global": ".gitignore_global",
    "karabiner/karabiner.edn": ".config/karabiner.edn",
    "Library/Application Support/Code - Insiders/User/keybindings.json": "vscode/keybindings.json",
    ".ideavimrc" : "idea/.vimrc",
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
    for name in vscode.extensions.names:
        os.system("code --install-extension %s" % name)


def install_brew():
    os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"') 


def install_brew_apps():
    for name in brew.apps.names:
        try:
            os.system("brew list %s" % name)
            print("%s already installed" % name)
        except Exception:
            os.system("brew install %s" % name)


def open_app_urls():
    for url in apps.urls:
        os.system("open %s" % url)


if __name__ == "__main__":
    create_symlinks()
import apps

import os
import argparse

src_dst_sym = {
    "zsh/zshrc.zsh": ".zshrc",
    "git/gitconfig": ".gitconfig",
    "git/gitignore_global": ".gitignore",
    "karabiner/karabiner.edn": ".config/karabiner.edn",
    "idea/.vimrc":".ideavimrc",
    "vim/.vimrc":".vimrc",
    "vscode/settings.json": "Library/Application Support/Code/User/settings.json"
}


def make_dirs_for_file(fp: str):
    dir_path = os.path.join(*os.path.split(fp)[:-1])
    os.makedirs(dir_path, exist_ok=True)


def create_symlinks():
    home_dir = os.getenv("HOME")
    dot_dir = os.path.join(home_dir, "dotfiles")
    cache_dir = os.path.join(home_dir, '.cache')

    for src_fname, dst_fname in src_dst_sym.items():
        src = os.path.join(dot_dir, src_fname)
        dst = os.path.join(home_dir, dst_fname)
        if os.path.isfile(dst) is True:
            msg = "File '%s' exists\nYes(y) to overwrite (old moved to %s): " % (dst, cache_dir)
            if input(msg).lower() not in ['yes', 'y']:
                print("skipping\n")
                continue
            cache = os.path.join(cache_dir, dst_fname)
            make_dirs_for_file(cache)
            os.replace(dst, cache)

        make_dirs_for_file(dst)
        os.symlink(src, dst)
        print("created symlink\n  from:'%s'\n  to:'%s'\n" % (src, dst))


def install_vscode_extensions():
    """requires VSCode command line tools"""
    for name in apps.vscode_extension:
        os.system("code --install-extension %s" % name)


def install_brew():
    os.system(
        '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')


def install_brew_apps():
    for name in apps.brew:
        os.system("brew install %s" % name)


def open_app_urls():
    for url in apps.urls:
        os.system("open %s" % url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("mac config setup")

    # (VSCode and Karabiner need to be installed)
    parser.add_argument("--apps", help="opens urls for apps that need manual installation",
                        action="store_true")
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

    if args.vscode_ext:
        install_vscode_extensions()

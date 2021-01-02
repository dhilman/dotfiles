# setting terminal to Pro theme
defaults write com.apple.Terminal "Default Window Settings" -string "Pro"
defaults write com.apple.Terminal "Startup Window Settings" -string "Pro"
echo 'Terminal theme set to Pro'

# https://www.howtogeek.com/267463/how-to-enable-key-repeating-in-macos.
defaults write -g ApplePressAndHoldEnabled -bool false
echo 'Fast key repeat. Requires restart.'

# https://twitter.com/jordwalke/status/1230582824224165888 fast repeat.
defaults write NSGlobalDomain KeyRepeat -int 1

defaults write -g NSAutomaticWindowAnimationsEnabled -bool false
echo 'Fast opening and closing windows and popovers'

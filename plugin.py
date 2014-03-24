__module_name__ = "rhythmbox"
__module_version__ = "1.1"
__module_description__ = "Plugin for Rhythymbox integration"

import hexchat
import subprocess


def np(word, word_eol, userdata):
    output = subprocess.check_output([
        'rhythmbox-client',
        '--print-playing-format',
        '%tt - %ta'
    ])
    output = output.strip()  # Has a trailing newline
    hexchat.command('me NP: %s' % output)
    return hexchat.EAT_ALL

hexchat.hook_command('np', np)

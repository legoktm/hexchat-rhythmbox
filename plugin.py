__module_name__ = "rhthymbox"
__module_version__ = "1.0"
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

hexchat.hook_command('np', np)

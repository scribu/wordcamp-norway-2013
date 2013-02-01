import subprocess

def get_wp_option(key):
    command = ["wp", "option", "get", key]

    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    out, err = proc.communicate()

    return out.strip("\n")

print get_wp_option("home")

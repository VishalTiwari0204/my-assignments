#
# This file implements assignments given by ful.io
# Date Created: 26-Nov-2022 
# Last Updated: 26-Nov-2022
# Author : Vishal Tiwari 

# Assignments: It is available in doc/

import subprocess

def run_command(cmd):
    """ This function works as running command
    Argument:
        cmd (str) Input command
    Retrurn :
        Return is output of command
    """
    cmd = cmd.split()
    p = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT
        )

    r = p.communicate()[0].decode(errors="ignore")
    if p.returncode not in [0, 1]:
        print(f"Failed command: {cmd}")

    return r

def extract_email_and_phone(whois_output):
    """ This function works as extracting the Emails and Phone No. 
    Arguments:
        whois_output (str) Output of whois command 
    Returns:
        Phone No. and Emails 
    """
    # Regex for Phone No. 
    pattern_phone_no = re.compile("[+]?\d{0,3}[.\s]\d{10}")
    phone_no = (re.findall(pattern_phone_no, whois_output))

    # Regex For Email 
    pattern_email = "[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}"
    email = (re.findall(pattern_email, whois_output))
    return phone_no, email

def process_whois_info(site_name):
    command = "whois "+site_name
    print("command: ",command) 
    whois_output = run_command(command)
    phone_no, email = extract_email_and_phone(whois_output)
    print("Phone No. and Email",phone_no, email)


if __name__ == '__main__':

    process_whois_info('ful.io')


#!/bin/python3

# Quick-n-dirty Version (might eat memory or lock up after some time)
# Purpose of this tool:
# Transform APT History Logs, Widnows DNS-Logs or other multiline logs into handy one-liners

# Windows DNS-Logs
# HEADER_MARKER = 'NOERROR'
# ESCALATION_MARKER = 'ANSWER'
# DATA_MARKER_A = 'DATA'
# DATA_MARKER_B = '.'

# APT History Log
HEADER_MARKER = 'Start-Date'
ESCALATION_MARKER = '(1000)'
DATA_MARKER_A = 'End-Date'
DATA_MARKER_B = ':'

MAX_MATCHES_PER_FILE = 10000

def filter_logs(in_file, out_file):
    match_count = 0
    with open(in_file, 'r') as in_f:
        with open(out_file, 'w') as out_f:
            status = 0
            tmp_line: str = ''

            while match_count < MAX_MATCHES_PER_FILE:
                try:
                    in_data = in_f.readline()

                    # Start Block
                    if in_data == '\n':
                        tmp_line = ''
                        status = 1

                    if (status == 1) and (HEADER_MARKER in in_data):
                        tmp_line += in_data.replace('\n', ' ')
                        status = 2

                    if (status == 2) and (ESCALATION_MARKER in in_data):
                        # we don't need this line, just set flag
                        # tmp_line += in_data.replace('\n', ' ')
                        status = 3

                    if (status == 3) and (DATA_MARKER_A in in_data) and (DATA_MARKER_B in in_data):
                        tmp_line += in_data
                        status = 0

                        out_f.writelines([tmp_line])

                except IOError:
                    break

            out_f.close()
        in_f.close()


filter_logs('history.log', 'history_filtered.log')

exit()

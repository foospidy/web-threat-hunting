"""
Calculate average respones size by method and url.
"""
import sys
import apache_log_parser

DATA = {}
AVERAGES = {}
COUNTS = {}
METHOD = "POST"
LOG_FORMAT = "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\""

with open(sys.argv[1], "r") as log:
    for line in log:
        line_parser = apache_log_parser.make_parser(LOG_FORMAT)
        line_values = line_parser(line)

        if line_values['request_method'] == METHOD and line_values['status'] == "200":
            if line_values['request_url'] in DATA:
                DATA[line_values['request_url']].append(int(line_values['response_bytes_clf']))
            else:
                DATA[line_values['request_url']] = [int(line_values['response_bytes_clf'])]

for k, v in DATA.items():
    AVERAGES[k] = sum(v) / float(len(v))
    COUNTS[k] = len(v)

for k, v in AVERAGES.items():
    print('{} {} {}'.format(k, COUNTS[k], v))

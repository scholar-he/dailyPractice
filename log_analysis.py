#! /usr/bin/python
# _*_coding:utf8_*_

"""
Author:

Date:
    2020/12/8 20:40
Description:
    1. read the specified log file
    2. count num '404' occoured
    3. record line with '404' to a new file
"""
import logging
from absl import app
from absl import flags
from datetime import datetime

FLAGS = flags.FLAGS
flags.DEFINE_string('path', None, 'Specify the log directory')
flags.DEFINE_string('output', '/home/', 'Specify the output path')

# mark arg 'path' as required
flags.mark_flag_as_required('path')

def main(unused_arg):
    logging.info("log analysis start")
    log_path = FLAGS.path
    output = FLAGS.output
    record = list() # record line with '404'
    count = 0 # count num '404' occoured
    # read log file
    with open(log_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "404" in line:
                count += 1
                record.append(line)
    # write to file
    datestr = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = '{}log_analysis-{}.log'.format(output, datestr)
    logging.info('output file path: {}'.format(output_file))
    with open(output_file, 'w') as f:
        first_line = "total '404' nums: {}\n".format(count)
        f.write(first_line)
        for line in record:
            f.write(line)

    logging.info("log analysis complete")


if __name__ == '__main__':
    app.run(main)

from time import time


def log_state(heat_pseudo_temp, humidity, current_temp, desired_temp, heat_state=None):
    heat_state = '\t' if heat_state is None else \
        '%.1f\t' % heat_pseudo_temp if heat_state else '\t%.1f' % heat_pseudo_temp
    line = '{:.2f}\t{:.1f}\t{:.1f}\t{}\t{}\n'.format(time(), humidity, current_temp, desired_temp, heat_state)
    try:
        with open('log.txt', 'a') as log:
            log.write(line)
    except OSError as e:
        pass

def log_event(event):
    with open('event_log.txt', 'a') as log_file:
        log_file.write(event + "\n")

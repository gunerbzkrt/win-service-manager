import win32serviceutil
import time
import logging

# Logging Hierarchy
# NOTSET
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# Set the logging level to INFO
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


# Status for Windows service
# SERVICE_STOPPED: 1
# SERVICE_START_PENDING: 2
# SERVICE_STOP_PENDING: 3
# SERVICE_RUNNING: 4
# SERVICE_CONTINUE_PENDING: 5
# SERVICE_PAUSE_PENDING: 6
# SERVICE_PAUSED: 7


# Stop Service if it's running
def stop_service(service_name):
    # Query the status of the service
    status = win32serviceutil.QueryServiceStatus(service_name)
    # Check if service is running
    if status[1] == 4:
        # Stop service if it's running
        win32serviceutil.StopService(service_name)
        logging.info(f"'{service_name}' service has been stopped.")
        # Wait for service stop
        while True:
            # Query the status of the service
            status = win32serviceutil.QueryServiceStatus(service_name)
            # If the service is stopped, break out of the loop
            if status[1] == 1:
                break
            # Wait for 1 second before querying the service again
            time.sleep(1)
    else:
        logging.info(f"'{service_name}' service is already stopped.")

# Start Service if it's running
def start_service(service_name):
    # Query the status of the service
    status = win32serviceutil.QueryServiceStatus(service_name)
    # Check if service is stopped
    if status[1] == 1:
        # Start service if it's stopped
        win32serviceutil.StartService(service_name)
        logging.info(f"'{service_name}' Service have been started")
        # Wait for service stop
        while True:
            # Query the status of the service
            status = win32serviceutil.QueryServiceStatus(service_name)
            # If the service is stopped, break out of the loop
            if status[1] == 4:
                break
            # Wait for 1 second before querying the service again
            time.sleep(1)
    else:
        logging.info(f"'{service_name}' Service is already running.")

# Restart Service
def restart_service(service_name):
    # Query the status of the service
    status = win32serviceutil.QueryServiceStatus(service_name)
    # Check if service is running
    if status[1] == 4:
        # Stop service if it's running
        win32serviceutil.RestartService(service_name)
        logging.info(f"'{service_name}' service has been restarted.")
        # Wait for service stop
        while True:
            # Query the status of the service
            status = win32serviceutil.QueryServiceStatus(service_name)
            # If the service is running, break out of the loop
            if status[1] == 4:
                break
            # Wait for 1 second before querying the service again
            time.sleep(1)
    else:
        logging.info(f"'{service_name}' is not running. The service should be run to restart it..")

# Remove service if it's running      
def remove_service(service_name):
    try:
        # Check if the service exists
        status = win32serviceutil.QueryServiceStatus(service_name)
        # Check if the service is running
        if status[1] == 4:
            # Stop service
            stop_service(service_name)
            # Wait for 1 second before removing the service
            time.sleep(1)
        # Remove the service
        win32serviceutil.RemoveService(service_name)
        try:
            # Check if service is deleted
            status = win32serviceutil.QueryServiceStatus(service_name)
        except Exception as e:
            # If the service does not exists
            logging.info(f"'{service_name}' has been removed.")
    except Exception as e:
        logging.warning(f"{e.args[2]}")

# Check status of service
def status_service(service_name):
    # Possible service status
    status = {
        1:"SERVICE_STOPPED",
        2:"SERVICE_START_PENDING",
        3:"SERVICE_STOP_PENDING",
        4:"SERVICE_RUNNING",
        5:"SERVICE_CONTINUE_PENDING",
        6:"SERVICE_PAUSE_PENDING",
        7:"SERVICE_PAUSED"
    }

    # Query for service status
    query_status = win32serviceutil.QueryServiceStatus(service_name)
    status_index = query_status[1]
    # Return services status based on index
    return status.get(status_index,"Unknown status index")

# Install service
def install_service(service_path,service_name):
    # Install the service
    win32serviceutil.InstallService(service_path, service_name ,displayName=service_name)

    try:
        status = win32serviceutil.QueryServiceStatus(service_name)
        logging.info(f"'{service_name}' has been installed as a service.")
    except Exception as e:
        logging.info(f"'{service_name}' has not been installed. {e.args[2]}")





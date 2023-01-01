# Windows Service Manager


A Python script for managing Windows services. This script provides an easy way to manage Windows services in Python. It allows you to start, stop, restart, install and remove a service, as well as query the status of a service.

## Installation
To use this script, you will need to have Python installed on your system. You will also need to install the Python for Windows extensions package, which can be done using pip:


```bash
pip install pywin32
```


## Usage
To use the script, import it in your Python code and call the relevant function with the name of the service you want to manage as a string argument.

```python
import win_service_manager

# Stop a service named "MyService"
win_service_manager.stop_service('MyService')

# Start a service named "MyOtherService"
win_service_manager.start_service('MyOtherService')
```

## Available functions
* start_service(service_name: str) -> None: Start a service.
* stop_service(service_name: str) -> None: Stop a service.
* restart_service(service_name: str) -> None: Restart a service.
* remove_service(service_name: str) -> None: Remove a service.
* status_service(service_name: str) -> None: Status of a service.
* install_service(service_path: str, service_name: str) --> None: Install a service.


## Error handling
The script includes error handling using the pywintypes.error exception class, which is raised when a Windows function call fails. This allows you to catch any errors that may occur and take appropriate action, such as logging the error or retrying the operation.

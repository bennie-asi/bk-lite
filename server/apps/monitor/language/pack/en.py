MONITOR_OBJECT_TYPE = {
    "OS": "OS",
    "Web": "Web",
    "Middleware": "Middleware",
    "Database": "Database",
    "K8S": "K8S",
    "Network Device": "Network Device",
    "Hardware Device": "Hardware Device",
    "Container Management": "Container Management",
    "Other": "Other",
    "VMware": "VMware",
    "Tencent Cloud": "Tencent Cloud"
}

MONITOR_OBJECT = {
    "Host": "Host",
    "Website": "Website",
    "Ping": "Ping",
    "RabbitMQ": "RabbitMQ",
    "Nginx": "Nginx",
    "Apache": "Apache",
    "ClickHouse": "ClickHouse",
    "Consul": "Consul",
    "Tomcat": "Tomcat",
    "Zookeeper": "Zookeeper",
    "ActiveMQ": "ActiveMQ",
    "ElasticSearch": "ElasticSearch",
    "MongoDB": "MongoDB",
    "Mysql": "Mysql",
    "Postgres": "Postgres",
    "Redis": "Redis",
    "Switch": "Switch",
    "Router": "Router",
    "Loadbalance": "Loadbalance",
    "Firewall": "Firewall",
    "Detection Device": "Detection Device",
    "Bastion Host": "Bastion Host",
    "Scanning Device": "Scanning Device",
    "Storage": "Storage",
    "Hardware Server": "Hardware Server",
    "Docker": "Docker",
    "Docker Container": "Docker Container",
    "Cluster": "Cluster",
    "Pod": "Pod",
    "Node": "Node",
    "SNMP Trap": "SNMP Trap",
    "vCenter": "vCenter",
    "ESXI": "ESXI",
    "VM": "VM",
    "DataStorage": "DataStorage",
    "JVM": "JVM",
    "Jetty": "Jetty",
    "WebLogic": "WebLogic",
    "TCP": "Tencent Cloud Platform",
    "CVM": "CVM",
    "Oracle": "Oracle",
    "Minio": "Minio"
}

MONITOR_OBJECT_PLUGIN = {
    "Host": {
        "name": "Host",
        "desc": "The host monitoring plugin is used to collect and analyze the performance data of the host, including CPU, memory, disk, and network usage."
    },
    "Website": {
        "name": "Website Monitoring",
        "desc": "The website monitoring plugin is used to periodically check the availability and performance of HTTP/HTTPS connections."
    },
    "Ping": {
        "name": "Ping",
        "desc": "Ping is used to check the connectivity and response time of a target host or network device by sending ICMP Echo requests."
    },
    "K8S": {
        "name": "K8S",
        "desc": "The K8S monitoring plugin is used to monitor the status and health of Kubernetes clusters, including performance metrics of nodes, containers, and pods."
    },
    "Switch SNMP General": {
        "name": "Switch General (SNMP)",
        "desc": "The SNMP General plugin is used to monitor and manage the status of switches via SNMP. Administrators can obtain key information about the device, such as interface traffic, error statistics, and status information, to optimize network performance and improve management efficiency."
    },
    "Router SNMP General": {
        "name": "Router General (SNMP)",
        "desc": "The SNMP General plugin is used to monitor and manage the status of routers via SNMP. Administrators can obtain key information about the device, such as interface traffic, error statistics, and status information, to optimize network performance and improve management efficiency."
    },
    "Loadbalance SNMP General": {
        "name": "Load Balancer General (SNMP)",
        "desc": "The SNMP General plugin is used to monitor and manage the status of load balancers via SNMP. Administrators can obtain key information about the device, such as interface traffic, error statistics, and status information, to optimize network performance and improve management efficiency."
    },
    "Firewall SNMP General": {
        "name": "Firewall General (SNMP)",
        "desc": "The SNMP General plugin is used to monitor and manage the status of firewalls via SNMP. Administrators can obtain key information about the device, such as interface traffic, error statistics, and status information, to optimize network performance and improve management efficiency."
    },
    "Detection Device SNMP General": {
        "name": "Detection Device General (SNMP)",
        "desc": "The SNMP General plugin is used to monitor and manage the status of detection devices via SNMP. Administrators can obtain key information about the device, such as interface traffic, error statistics, and status information, to optimize network performance and improve management efficiency."
    },
    "Bastion Host SNMP General": {
        "name": "Bastion Host General (SNMP)",
        "desc": "The SNMP General plugin is used to monitor and manage the status of bastion hosts via SNMP. Administrators can obtain key information about the device, such as interface traffic, error statistics, and status information, to optimize network performance and improve management efficiency."
    },
    "Scanning Device SNMP General": {
        "name": "Scanning Device General (SNMP)",
        "desc": "The SNMP General plugin is used to monitor and manage the status of scanning devices via SNMP. Administrators can obtain key information about the device, such as interface traffic, error statistics, and status information, to optimize network performance and improve management efficiency."
    },
    "Storage SNMP General": {
        "name": "Storage Device General (SNMP)",
        "desc": "The SNMP General plugin is used to monitor and manage the status of storage devices via SNMP. Administrators can obtain key information about the device, such as interface traffic, error statistics, and status information, to optimize network performance and improve management efficiency."
    },
    "Storage IPMI": {
        "name": "Storage Device General (IPMI)",
        "desc": "The IPMI monitoring plugin communicates with hardware to provide real-time monitoring of system health status, hardware sensor data, and power management."
    },
    "Hardware Server SNMP General": {
        "name": "Hardware Server General (SNMP)",
        "desc": "The SNMP General plugin is used to monitor and manage the status of hardware servers via SNMP. Administrators can obtain key information about the device, such as interface traffic, error statistics, and status information, to optimize network performance and improve management efficiency."
    },
    "Hardware Server IPMI": {
        "name": "Hardware Server General (IPMI)",
        "desc": "The IPMI monitoring plugin communicates with hardware to provide real-time monitoring of system health status, hardware sensor data, and power management."
    },
    "SNMP Trap": {
        "name": "SNMP Trap",
        "desc": "The SNMP Trap monitoring plugin is used to receive and process alarms or status notifications (Trap messages) actively pushed by network devices, enabling real-time monitoring and fault alerts."
    },
    "Zookeeper": {
        "name": "Zookeeper",
        "desc": "By collecting runtime performance data and stability metrics of Zookeeper, such as uptime, average latency, and read-write ratios, users can monitor the cluster status in real-time and optimize performance."
    },
    "Apache": {
        "name": "Apache",
        "desc": "Real-time collection of Apache runtime data, resource utilization, request processing efficiency, and bandwidth statistics, helping users optimize performance, diagnose issues, and achieve efficient operations management."
    },
    "ClickHouse": {
        "name": "ClickHouse",
        "desc": "Collect runtime metrics of ClickHouse instances, such as memory, disk, query events, etc., for performance monitoring, resource tracking, and fault diagnosis, ensuring stable database operation."
    },
    "RabbitMQ": {
        "name": "RabbitMQ",
        "desc": "Used for monitoring RabbitMQ's runtime status, resource usage, message flow, and queue health."
    },
    "ActiveMQ": {
        "name": "ActiveMQ",
        "desc": "Used for collecting ActiveMQ topic-related metrics, enabling real-time monitoring of consumer count, enqueue/dequeue rates, and topic message backlog to ensure stable message queue operation."
    },
    "Nginx": {
        "name": "Nginx",
        "desc": "By collecting metrics such as Nginx requests, connection status, and processing efficiency, this helps monitor and optimize the website's performance and stability."
    },
    "Tomcat": {
        "name": "Tomcat",
        "desc": "Collects key performance metrics of Tomcat connectors and JVM memory to monitor server resource usage, request processing efficiency, and errors, optimizing system performance."
    },  
    "Consul": {
        "name": "Consul",
        "desc": "Used for real-time monitoring of Consul service health, collecting status check results, analyzing passing, warning, and critical metrics to help users promptly identify issues and ensure service availability."
    },
    "ElasticSearch": {
        "name": "ElasticSearch",
        "desc": "By collecting Elasticsearch file system metrics, HTTP requests, IO statistics, document statistics, query cache, and circuit breaker metrics, this plugin helps users monitor the health and performance of their cluster."
    },
    "MongoDB": {
        "name": "MongoDB",
        "desc": "By collecting metrics on MongoDB read and write activities, command execution, connection counts, latency, memory usage, and network traffic, this helps optimize performance and ensure efficient and stable database operations."
    },
    "Mysql": {
        "name": "Mysql",
        "desc": "Used to collect and monitor key metrics for MySQL database health and performance."
    },
    "Postgres": {
        "name": "Postgres",
        "desc": "Collecting PostgreSQL's session management, transaction metrics, and I/O performance data helps monitor resource usage, access behavior, operational efficiency, and identify potential issues within the database."
    },
    "Redis": {
        "name": "Redis",
        "desc": "Used to collect key indicators of Redis performance and resource utilization, helping improve system efficiency and stability."
    },
    "Docker": {
        "name": "Docker",
        "desc": "Used for collecting and analyzing the status, resource usage (CPU, memory, network, IO), and performance metrics of Docker containers, helping to identify anomalies and optimize container operational efficiency."
    },
    "vCenter": {
        "name": "vCenter",
        "desc": "vCenter is VMware's virtualization hub for monitoring resources (CPU/memory/storage/network), analyzing performance, and optimizing configurations. It helps identify VM/host anomalies and improves environment efficiency."
    },
    "JVM": {
        "name": "JVM",
        "desc": "Used for collecting and analyzing the runtime status, memory usage (heap, non-heap, buffer pool), thread activity, garbage collection, and system resource metrics (CPU, physical memory, swap space) of the JVM (Java Virtual Machine), helping to identify performance bottlenecks, detect memory leaks, and optimize Java application performance."
    },
    "ActiveMQ-JMX": {
        "name": "ActiveMQ-JMX",
        "desc": "This ActiveMQ plugin uses JMX for collection, obtaining key performance metrics like message queues, connection pools, and message throughput. It monitors message processing efficiency and resource usage in real-time, optimizing system performance and ensuring service stability."
    },
    "Jetty-JMX": {
        "name": "Jetty-JMX",
        "desc": "Collects key performance metrics of Jetty task processing, thread pools, network connections, HTTP configurations, and JMX self-monitoring to track server resource usage, task handling capabilities, and connection status—enabling optimized system performance and improved service stability."
    },
    "Tomcat-JMX": {
        "name": "Tomcat-JMX",
        "desc": "Collects Tomcat key performance metrics via JMX, including thread pools, HTTP connections, JVM memory, and request latency, to monitor operational status and resource efficiency for performance optimization and fault detection."
    },
    "WebLogic-JMX": {
        "name": "WebLogic-JMX",
        "desc": "This plugin uses JMX to collect WebLogic's key metrics, including thread pools, connection pools, memory, EJB, Servlet, JMS performance, and Web service response times. It enables real-time monitoring, performance optimization, and risk early warning to ensure system stability."
    },
    "Tencent Cloud": {
        "name": "Tencent Cloud",
        "desc": "It is used to collect various monitoring index data of Tencent Cloud in real - time, covering dimensions such as computing resources, network performance, and storage usage, helping users gain in - depth insights into resource status, accurately locate anomalies, and efficiently complete operation and maintenance management and cost optimization.​"
    },
    "Oracle-Exporter": {
        "name": "Oracle-Exporter",
        "desc": "It is used to collect metrics on Oracle's uptime, operation counts, transaction commits/rollbacks, and various wait times in real-time via the exporter method, assisting users in health checks and performance tuning.​"
    },
    "Minio": {
        "name": "Minio",
        "desc": "Collects key metrics of the Minio object storage system, including runtime status, storage capacity, usage, replication, inter-node communication, and S3 requests, enabling real-time monitoring of storage health, performance optimization, and anomaly detection. ​"
    }
}

MONITOR_OBJECT_METRIC_GROUP = {
    "Host": {
        "CPU": "CPU",
        "System": "System", 
        "Disk IO": "Disk IO", 
        "DISK": "Disk",
        "Process": "Process",
        "MEMORY": "Memory",
        "Net": "Net",
    },
    "Website": {
        "HTTP": "HTTP",
    },
    "Ping": {
        "Ping": "Ping",
    },
    "Cluster": {
        "Counts": "Counts",
        "Utilization": "Utilization",
    },
    "Pod": {
        "Status": "Status",
        "CPU": "CPU",
        "Memory": "Memory",
        "Disk": "Disk",
        "Network": "Network",
    },
    "Node": {
        "Status": "Status",
        "CPU": "CPU",
        "Memory": "Memory",
        "Disk": "Disk",
        "Net": "Net",
        "Load": "Load",
    },
    "Switch": {
        "Base": "Base",
        "Status": "Status",
        "Bandwidth": "Bandwidth",
        "Packet Error": "Packet Error",
        "Packet Loss": "Packet Loss",
        "Packet": "Packet",
        "Traffic": "Traffic",
    },
    "Router": {
        "Base": "Base",
        "Status": "Status",
        "Bandwidth": "Bandwidth",
        "Packet Error": "Packet Error",
        "Packet Loss": "Packet Loss",
        "Packet": "Packet",
        "Traffic": "Traffic",
    },
    "Loadbalance": {
        "Base": "Base",
        "Status": "Status",
        "Bandwidth": "Bandwidth",
        "Packet Error": "Packet Error",
        "Packet Loss": "Packet Loss",
        "Packet": "Packet",
        "Traffic": "Traffic",
    },
    "Firewall": {
        "Base": "Base",
        "Status": "Status",
        "Bandwidth": "Bandwidth",
        "Packet Error": "Packet Error",
        "Packet Loss": "Packet Loss",
        "Packet": "Packet",
        "Traffic": "Traffic",
    },
    "Detection Device": {
        "Base": "Base",
        "Status": "Status",
        "Bandwidth": "Bandwidth",
        "Packet Error": "Packet Error",
        "Packet Loss": "Packet Loss",
        "Packet": "Packet",
        "Traffic": "Traffic",
    },
    "Bastion Host": {
        "Base": "Base",
        "Status": "Status",
        "Bandwidth": "Bandwidth",
        "Packet Error": "Packet Error",
        "Packet Loss": "Packet Loss",
        "Packet": "Packet",
        "Traffic": "Traffic",
    },
    "Scanning Device": {
        "Base": "Base",
        "Status": "Status",
        "Bandwidth": "Bandwidth",
        "Packet Error": "Packet Error",
        "Packet Loss": "Packet Loss",
        "Packet": "Packet",
        "Traffic": "Traffic",
    },
    "Storage": {
        "Base": "Base",
        "Status": "Status",
        "Bandwidth": "Bandwidth",
        "Packet Error": "Packet Error",
        "Packet Loss": "Packet Loss",
        "Packet": "Packet",
        "Traffic": "Traffic",
         "Power": "Power", 
        "Environment": "Environment",       
    },
    "Hardware Server": {
        "Base": "Base",
        "Status": "Status",
        "Bandwidth": "Bandwidth",
        "Packet Error": "Packet Error",
        "Packet Loss": "Packet Loss",
        "Packet": "Packet",
        "Traffic": "Traffic",
        "Power": "Power", 
        "Environment": "Environment",            
    },
    "SNMP Trap": {   
    },
    "Zookeeper": {
        "Uptime": "Uptime",
        "Performance": "Performance",
        "Connection": "Connection",
        "Znode": "Znode",
        "Traffic": "Traffic",
    },
    "Apache": {
        "Uptime": "Uptime",
        "Work": "Work",
        "Request": "Request",
        "CPU": "CPU",
        "Duration": "Duration",
    },
    "ClickHouse": {
        "Uptime": "Uptime",
        "Memory": "Memory",
        "Disk": "Disk",
        "Query": "Query",
        "Part": "Part",
        "Load": "Load",
    },
    "RabbitMQ": {
        "Exchange": "Exchange",
        "Node": "Node",
        "Message": "Message",
    },
    "ActiveMQ": {
        "Topic": "Topic",
    },
    "Nginx": {
        "Request": "Request",
        "Connection": "Connection",
        "Efficiency": "Efficiency",
    },
    "Tomcat": {
        "Request": "Request",
        "Net": "Net",
        "Threads": "Threads",
        "Error": "Error",
        "JMX ": "JMX ",
    },
    "Consul": {
        "Check": "Check",
    },
    "ElasticSearch": {
        "Disk": "Disk",
        "HTTP": "HTTP",
        "IO": "IO",
        "Indices": "Indices",
        "Cache": "Cache",
        "Circuit Breakers": "Circuit Breakers",
    },
    "MongoDB": {
        "Active Operations": "Active Operations",
        "Commands": "Commands",
        "Connections": "Connections",
        "Latency": "Latency",
        "Memory": "Memory",
        "Traffic": "Traffic",
        "Storage": "Storage",
    },
    "Mysql": {
        "Connection": "Connection",
        "Error": "Error",
        "Cache": "Cache",
        "Traffic": "Traffic",
        "Command": "Command",
        "Session": "Session",
    },
    "Postgres": {
        "Performance": "Performance",
        "Cache": "Cache",
        "Memory": "Memory",
        "Transaction": "Transaction",
        "Session": "Session",
    },
    "Redis": {
        "Performance": "Performance",
        "Cache": "Cache",
        "Memory": "Memory",
        "Clients": "Clients",
        "CPU": "CPU",
        "Replication": "Replication",
        "Disk": "Disk",
        "Connectivity": "Connectivity",
    },
    "Docker": {
        "Docker Count": "Docker Count",
    },
    "Docker Container": {
        "Memory": "Memory",
        "CPU": "CPU",
        "Net": "Net",
        "Status": "Status",
        "IO": "IO",
    },
    "vCenter": {
        "Quantity": "Quantity",
    },
    "ESXI": {
        "Memory": "Memory",
        "CPU": "CPU",
        "Disk": "Disk",
        "Network": "Network",
    },
    "DataStorage": {
        "Default": "Default",
    },
    "VM": {
        "Memory": "Memory",
        "CPU": "CPU",
        "Disk": "Disk",
        "Network": "Network",
        "Power": "Power",
    },
    "JVM": {
        "JMXselfMonitor": "JMX Self-Monitoring Information",
        "Memory": "Memory",
        "Thread": "Thread",
        "OS": "Operating System",
        "BufferPool": "Buffer Pool",
        "GC": "Garbage Collection",
        "MemoryPool": "Memory Pool"
    },
    "ActiveMQ-JMX": {
        "Connection": "Connection",
        "Memory": "Memory",
        "Queue": "Queue",
        "Message": "Message",
        "Producer": "Producer",
        "Consumer": "Consumer",
        "Other": "Other",
        "JvmMemory": "JVM Memory",
        "JMXselfMonitor": "JMX Self-Monitoring Information"
    },
    "Jetty-JMX": {
        "Queuedthreadpool": "Queued Thread Pool",
        "JvmMemory": "JVM Memory",
        "Httpconfiguration": "HTTP Configuration",
        "Bufferpool": "Buffer Pool",
        "Serverconnector": "Server Connector",
        "Managedselector": "Managed Selector",
        "Reservedthread": "Reserved Thread",
        "JMXselfMonitor": "JMX Self-Monitoring Information"
    },
    "Tomcat-JMX": {
        "GlobalRequestProcessor": "Global Request Processing",
        "Threadpool": "Thread Pool",
        "Session": "Session",
        "JMXselfMonitor": "JMX Self-Monitoring Information"
    },
    "WebLogic-JMX": {
        "Threadpool": "Thread Pool",
        "Application": "Application",
        "WorkManager": "Work Manager",
        "JMS": "Messaging Service",
        "PersistentStore": "Persistent Storage",
        "JMXselfMonitor": "JMX Self-Monitoring Information"
    },
    "TCP": {

    },
    "CVM": {
        "CPU": "CPU",
        "Memory": "Memory",
        "Disk": "Disk",
        "Network": "Network"
    },
    "Oracle-Exporter": {
        "Base": "Base",
        "Activity": "Activity",
        "Wait": "Wait",
        "SGA": "SGA",
        "PGA": "PGA",
        "Tablespace": "Tablespace",
        "RAC": "RAC",
        "Process": "Process",
        "selfMonitor": "selfMonitor"
    },
    "Minio": {
        "Audit": "Audit",
        "ClusterCapacity": "Cluster Capacity",
        "ClusterDrive": "Cluster Drive",
        "ClusterHealth": "Cluster Health",
        "S3Request": "S3 Request",
        "BucketUsage": "Bucket Usage",
        "BucketRequests": "Bucket Requests",
        "DriveResource": "Drive Resource",
        "NetworkInterface": "Network Interface",
        "CPU": "CPU"
    }
}

MONITOR_OBJECT_METRIC = {
    "Host":{
    "cpu_summary.usage": {
        "name": "CPU Usage Rate",
        "desc": "Displays the CPU usage rate to indicate the system's load. It is derived by subtracting the idle from total. This metric is crucial for monitoring system performance."
    },
    "cpu_summary.idle": {
        "name": "CPU Idle Rate",
        "desc": "Displays the CPU idle rate, representing the amount of unused CPU resources in the system. It helps to know if the system is under high load. This metric is crucial for analyzing system performance and efficiency."
    },
    "cpu_summary.iowait": {
        "name": "Percentage of Time Waiting for IO",
        "desc": "Displays the percentage of CPU time spent waiting for IO operations, indicating the impact of disk or network performance on the system. Reducing wait time helps improve system performance. This metric is very useful for analyzing system bottlenecks."
    },
    "cpu_summary.system": {
        "name": "System Usage Rate",
        "desc": "Displays the system usage rate, showing the CPU resources consumed by kernel processes. Analyzing this value helps optimize system kernel performance and stability."
    },
    "cpu_summary.user": {
        "name": "User Usage Rate",
        "desc": "Displays the percentage of CPU resources used by user processes, helping understand the performance of applications and services. This metric is helpful in understanding the CPU consumption of specific applications."
    },
    "load1": {
        "name": "1 Minute Average Load",
        "desc": "Displays the average system load over the last 1 minute, providing a snapshot of short-term system activity. This metric helps monitor system performance in real-time."
    },
    "load5": {
        "name": "5 Minute Average Load",
        "desc": "Displays the average system load over the last 5 minutes, reflecting the medium-term load on the system. This medium-term metric helps identify sustained and intermittent high load situations."
    },
    "load15": {
        "name": "15 Minute Average Load",
        "desc": "Displays the average system load over the last 15 minutes, providing long-term load observation to understand the overall performance trend of the system."
    },
    "diskio_writes": {
        "name": "Disk I/O Write Rate",
        "desc": "Counts the number of data write operations to the disk in the specified time interval."
    },
    "diskio_write_bytes": {
        "name": "Disk I/O Write Bytes Rate",
        "desc": "Counts the number of bytes written to the disk in the specified time interval, represented in megabytes (MB)."
    },
    "diskio_write_time": {
        "name": "Disk I/O Write Time Rate",
        "desc": "Counts the time taken to write data to the disk in the specified time interval, represented in seconds (s)."
    },
    "diskio_reads": {
        "name": "Disk I/O Read Rate",
        "desc": "Counts the number of data read operations from the disk in the specified time interval."
    },
    "diskio_read_bytes": {
        "name": "Disk I/O Read Bytes Rate",
        "desc": "Counts the number of bytes read from the disk in the specified time interval, represented in megabytes (MB)."
    },
    "diskio_read_time": {
        "name": "Disk I/O Read Time Rate",
        "desc": "Counts the time taken to read data from the disk in the specified time interval, represented in seconds (s)."
    },
    "disk.is_use": {
        "name": "Disk Usage Rate",
        "desc": "Displays the percentage of disk space used, helping understand the utilization of disk resources. This metric is important for preventing disk overflow."
    },
    "disk.used": {
        "name": "Disk Used Size",
        "desc": "Displays the actual used disk space (in GB), used to determine disk capacity usage. This metric is helpful for monitoring disk space usage."
    },
    "env.procs": {
        "name": "Total Number of Processes",
        "desc": "Displays the total number of processes running on the system, helping understand the load distribution. This metric is important for monitoring the overall operation of the system."
    },
    "env.proc_running_current": {
        "name": "Number of Running Processes",
        "desc": "Displays the number of processes currently running, used to assess the concurrency. This metric is valuable for real-time monitoring of system load."
    },
    "env.procs_blocked_current": {
        "name": "Number of IO Blocked Processes",
        "desc": "Displays the number of processes currently blocked by IO operations. Analyzing this value helps optimize the system and reduce bottlenecks. This metric is helpful for identifying IO bottlenecks."
    },
    "mem.total": {
        "name": "Total Physical Memory Size",
        "desc": "Displays the total physical memory of the system (in GB), providing an overview of system resource configuration. This metric is important for understanding the base configuration of system resources."
    },
    "mem.free": {
        "name": "Free Physical Memory Amount",
        "desc": "Displays the amount of free physical memory currently available (in GB), helping understand the available resources. This metric is crucial for keeping track of memory resource usage."
    },
    "mem.cached": {
        "name": "Cache Memory Size",
        "desc": "Displays the amount of memory used for caching (in GB), used to improve system performance. This metric is important for understanding memory caching strategies."
    },
    "mem.buffer": {
        "name": "Buffer Memory Size",
        "desc": "Displays the amount of memory used for buffering (in GB), ensuring stable data transfer. This metric is crucial for performance optimization strategies."
    },
    "mem.usable": {
        "name": "Available Memory for Applications",
        "desc": "Displays the memory available for applications (in GB), ensuring smooth application operation. This metric is important for maintaining application performance and stability."
    },
    "mem.pct_usable": {
        "name": "Available Memory Percentage for Applications",
        "desc": "Displays the percentage of memory available, helping determine if there is sufficient memory to support applications. This metric is useful for monitoring memory pressure and capacity planning strategies."
    },
    "mem.used": {
        "name": "Memory Used by Applications",
        "desc": "Displays the memory used by applications (in GB), analyzing this value helps optimize application memory usage. This metric is crucial for monitoring application resource consumption."
    },
    "mem.pct_used": {
        "name": "Application Memory Usage Percentage",
        "desc": "Displays the percentage of memory used by applications, understanding memory usage distribution. This metric is valuable for optimizing memory usage."
    },
    "mem.psc_used": {
        "name": "Used Physical Memory Amount",
        "desc": "Displays the total amount of physical memory used by the system (in GB), helping understand the overall distribution of memory resources. This metric is crucial for gaining a comprehensive understanding of system memory usage."
    },
    "mem.shared": {
        "name": "Shared Memory Usage",
        "desc": "Displays the usage of shared memory (in GB), used for data sharing between processes. This metric helps optimize system memory allocation strategies."
    },
    "net.speed_packets_recv": {
        "name": "Incoming Packets on NIC",
        "desc": "Displays the number of data packets received by the network interface per unit of time, used to evaluate network reception performance. This metric is crucial for monitoring network traffic."
    },
    "net.speed_packets_sent": {
        "name": "Outgoing Packets on NIC",
        "desc": "Displays the number of data packets sent by the network interface per unit of time, used to evaluate network transmission performance. This metric is crucial for monitoring network traffic."
    },
    "net.speed_recv": {
        "name": "Incoming Bytes on NIC",
        "desc": "Displays the number of bytes received by the network interface per unit of time (in MB), used to evaluate network bandwidth utilization. This metric is important for monitoring network bandwidth."
    },
    "net.speed_sent": {
        "name": "Outgoing Bytes on NIC",
        "desc": "Displays the number of bytes sent by the network interface per unit of time (in MB), used to evaluate network bandwidth utilization. This metric is crucial for monitoring network bandwidth."
    },
    "net.errors_in": {
        "name": "NIC Error Packets",
        "desc": "Displays the number of error packets received by the network interface, used to detect network issues. This metric is helpful for identifying network faults and abnormal traffic."
    },
    "net.errors_out": {
        "name": "NIC Error Packets",
        "desc": "Displays the number of error packets sent by the network interface, helping understand network transmission errors. This metric is helpful for identifying network faults and abnormal traffic."
    },
    "net.dropped_in": {
        "name": "NIC Dropped Packets",
        "desc": "Displays the number of dropped packets received by the network interface, indicating network congestion. This metric is crucial for monitoring network reliability."
    },
    "net.dropped_out": {
        "name": "NIC Dropped Packets",
        "desc": "Displays the number of dropped packets sent by the network interface, indicating network transmission congestion. This metric is crucial for monitoring network reliability."
    },
    "nvidia_smi_memory_free": {
      "name": "GPU Memory Free",
      "desc": "The remaining capacity of GPU memory currently unoccupied, used to assess available resources."
    },
    "nvidia_smi_memory_used": {
      "name": "GPU Memory Used",
      "desc": "The capacity of GPU memory currently occupied, reflecting the memory size used by running tasks."
    },
    "nvidia_smi_memory_total": {
      "name": "GPU Memory Total",
      "desc": "The total capacity of GPU memory, indicating the maximum memory the device supports."
    },
    "nvidia_smi_utilization_memory": {
      "name": "GPU Memory Utilization",
      "desc": "The percentage of current memory usage, indicating the utilization of GPU memory resources (0%-100%), useful for optimizing memory allocation."
    },
    "nvidia_smi_power_draw": {
      "name": "GPU Power Draw",
      "desc": "The real-time power consumption of GPU, measured in watts (W), used to monitor energy consumption level."
    },
    "nvidia_smi_temperature_gpu": {
      "name": "GPU Core Temperature",
      "desc": "The operating temperature of the GPU core, measured in degrees Celsius (°C), used to monitor device status and safety."
    },
    "nvidia_smi_fan_speed": {
      "name": "GPU Fan Speed Percentage",
      "desc": "The percentage of current GPU fan speed relative to the maximum speed (0%-100%), used to monitor cooling condition and operational status."
    }
},
    "Website": {
    "http_success.rate": {
        "name": "Success Rate",
        "desc": "Measures the success rate of multiple nodes probing targets (the percentage of successful responses out of the total number of requests)."
    },
    "http_duration": {
        "name": "Response Time",
        "desc": "This metric represents the total time taken from initiating an HTTP request to receiving the HTTP response. It is used to assess the performance of web services, especially when handling user requests. An extended duration may indicate lower backend processing efficiency or network latency, which can adversely affect the user experience. It is crucial for enhancing system responsiveness and optimizing performance."
    },
    "http_code": {
        "name": "HTTP Code",
        "desc": "This metric represents the HTTP response status code for an HTTP request. It captures the value of the HTTP response status codes, such as 200 (OK), 404 (Not Found), 500 (Internal Server Error), etc. These status codes are vital for monitoring the health and performance of web applications, assisting in identifying potential issues."
    },
    "http_content.length": {
        "name": "HTTP Content Length",
        "desc": "This metric indicates the length of the HTTP response content in bytes. Larger content lengths can result in extended data transfer times and consume more bandwidth. Monitoring this metric is crucial for optimizing website performance or analyzing bandwidth usage. Understanding the size of the response content can assist developers in making optimizations."
    }
},
    "Ping":{
    "ping_ttl": {
        "name": "Average TTL",
        "desc": "Represents the average 'hop count' (or time) allowed for ping packets from the source device to the target. This metric helps identify if packets take an abnormal number of hops or if there are route anomalies. Higher TTL values indicate longer paths."
    },
    "ping_response_time": {
        "name": "Average Response Time",
        "desc": "Represents the average ping response time of the target device over a period. This metric helps evaluate latency between the source and target device. Lower average response time indicates good network performance."
    },
    "ping_packet_transmission_rate": {
        "name": "Packet Transmission Rate",
        "desc": "Represents the percentage of successfully received packets out of the total packets transmitted. This metric measures network quality and transmission reliability. Low packet loss indicates stable and reliable connectivity."
    },
    "ping_packet_loss_rate": {
        "name": "Packet Loss Rate",
        "desc": "Represents the percentage of packets lost during ping requests. This metric helps identify unstable network connections or transmission problems. Lower loss rates indicate more stable connectivity."
    },
    "ping_error_response_code": {
        "name": "Ping State",
        "desc": "Represents the resulting code after a ping operation. A code of 0 indicates success, while non-zero values indicate potential issues with the network or host. This metric helps quickly detect network connectivity errors."
    }
},
    "Cluster": {
        "cluster_pod_count": {
            "name": "Pod Count",
            "desc": "It is used to count the total number of Pods currently present in the Kubernetes cluster. This metric returns the count of Pods running in the cluster, including those across all namespaces."
        },
        "cluster_node_count": {
            "name": "Node Count",
            "desc": "It is used to count the total number of nodes currently available in the Kubernetes cluster. This metric returns the number of nodes in the cluster, helping users understand the scale and resources of the cluster."
        },
        "cluster_cpu_utilization": {
            "name": "CPU Utilization",
            "desc": "Represents the current CPU utilization of the cluster, typically expressed as a percentage."
        },
        "cluster_memory_utilization": {
            "name": "Memory Utilization",
            "desc": "Shows the current memory utilization of the cluster, expressed as a percentage."
        }
    },
    "Pod": {
        "pod_status": {
            "name": "Pod Status",
            "desc": "Retrieves the current status of the Pod, such as Running, Stopped, etc."
        },
        "pod_restart_count": {
            "name": "Restart Count",
            "desc": "Monitors the restart counts of containers in the Pod to assess stability and frequency of issues."
        },
        "pod_cpu_utilization": {
            "name": "CPU Utilization",
            "desc": "Calculates the CPU utilization of a Pod, reflecting the difference between container CPU limits and requests."
        },
        "pod_memory_utilization": {
            "name": "Memory Utilization",
            "desc": "Calculates the memory utilization of the Pod as a ratio of memory limits to requests."
        },
        "pod_io_writes": {
            "name": "I/O Write Rate",
            "desc": "This metric represents the number of I/O write operations performed by a specific Pod over a specified time period. The write count can help analyze the write demands of the application on the storage system."
        },
        "pod_io_read": {
            "name": "I/O Read Rate",
            "desc": "This metric represents the number of I/O read operations performed by a specific Pod over a specified time period. The read count can help analyze the read demands of the application on the storage system."
        },
        "pod_network_in": {
            "name": "Network In",
            "desc": "Monitors the inbound network traffic of a Pod, calculated based on the number of containers and IPs."
        },
        "pod_network_out": {
            "name": "Network Out",
            "desc": "Monitors the outbound network traffic of a Pod, calculated based on the number of containers and IPs."
        }
    },
    "Node": {
  "node_status_condition": {
    "name": "Node Status",
    "desc": "Node Status indicates the current operational state of the node, such as 'Running' or 'Stopped.' It helps administrators monitor and manage nodes within the Kubernetes cluster."
  },
  "node_cpu_utilization": {
    "name": "CPU Utilization",
    "desc": "CPU Utilization indicates the current usage level of the node's CPU relative to its total available CPU resources. Monitoring this metric helps identify CPU bottlenecks and optimize resource allocation."
  },
  "node_memory_usage": {
    "name": "Application Memory Usage",
    "desc": "Application Memory Usage represents the total amount of memory utilized by applications running on the node. This metric helps understand the memory demands of applications and their impact on system performance."
  },
  "node_memory_utilization": {
    "name": "Application Memory Utilization Rate",
    "desc": "Application Memory Utilization Rate is the ratio of memory used by the application to its configured memory limits. By monitoring this metric, users can determine if adjustments to memory limits are needed."
  },
  "node_io_read": {
    "name": "Disk Write Rate",
    "desc": "Disk Write Rate indicates the rate of write operations performed by the node over a specified period. This metric is crucial for monitoring the disk write performance of applications."
  },
  "node_io_write": {
    "name": "Disk Read Rate",
    "desc": "Disk Read Rate indicates the rate of read operations performed by the node over a specified period. This metric helps assess the data reading performance of applications and storage load."
  },
  "node_network_receive": {
    "name": "Incoming Bytes on NIC",
    "desc": "Network In refers to the volume of data traffic received through the network interface. Monitoring this metric helps analyze if network bandwidth is sufficient and the overall network performance."
  },
  "node_network_transmit": {
    "name": "Outgoing Bytes on NIC",
    "desc": "Network Out refers to the volume of data traffic sent through the network interface. This metric helps understand the node's network egress demands and potential bottlenecks."
  },
  "node_cpu_load1": {
    "name": "1 Minute Average Load",
    "desc": "1 Minute Average Load indicates the average load on the system over the last minute. This metric helps provide a real-time understanding of the system’s load level."
  },
  "node_cpu_load5": {
    "name": "5 Minute Average Load",
    "desc": "5 Minute Average Load indicates the average load on the system over the last 5 minutes. This metric helps identify load trends and their impact on system performance."
  },
  "node_cpu_load15": {
    "name": "15 Minute Average Load",
    "desc": "15 Minute Average Load indicates the average load on the system over the last 15 minutes. Monitoring this metric helps administrators understand the long-term load state of the system."
  }
    },
    "Switch": {
  "sysUpTime": {
    "name": "System Uptime",
    "desc": "This metric indicates the uptime of the device since the last restart, measured in days. By monitoring the uptime, network administrators can understand the stability and reliability of the device and identify potential reboot or failure issues."
  },
  "ifAdminStatus": {
    "name": "Interface Admin Status",
    "desc": "This metric indicates the administrative status of the network switch interface. It serves to indicate whether the interface is enabled (up) or disabled (down) by an administrator, along with other states such as testing or not present. This information is vital for network management and troubleshooting."
  },
  "ifOperStatus": {
    "name": "Interface Oper Status",
    "desc": "This metric reflects the actual operational status of the network switch interface, indicating whether the interface is operational. Unlike the administrative status, the operational status shows whether the interface can successfully receive and send traffic, which is crucial for monitoring network health."
  },
  "ifHighSpeed": {
    "name": "Interface Bandwidth",
    "desc": "This metric indicates the maximum data transmission speed supported by the network interface, usually measured in KB per second. Understanding the maximum speed of the interface helps administrators optimize traffic and utilize network resources effectively."
  },
  "ifInErrors": {
    "name": "Incoming Errors Rate (per second)",
    "desc": "This metric calculates the average rate of incoming error packets over the past 5 minutes, measured in packets per second. Monitoring incoming errors allows administrators to detect potential issues, such as physical connection faults or configuration errors, in a timely manner."
  },
  "ifOutErrors": {
    "name": "Outgoing Errors Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing error packets over the past 5 minutes, measured in packets per second. Monitoring outgoing errors is essential for identifying transmission issues and ensuring data integrity."
  },
  "ifInDiscards": {
    "name": "Incoming Discards Rate (per second)",
    "desc": "This metric represents the average rate of incoming discarded packets over the past 5 minutes, measured in packets per second. Packet discards may indicate network congestion or resource shortages, and monitoring this metric can help administrators optimize network performance."
  },
  "ifOutDiscards": {
    "name": "Outgoing Discards Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing discarded packets over the past 5 minutes, measured in packets per second. Monitoring outgoing discards can help identify network transmission issues and misconfigurations."
  },
  "ifInUcastPkts": {
    "name": "Incoming Unicast Packets Rate (per second)",
    "desc": "This metric indicates the average rate of incoming unicast packets over the past 5 minutes, measured in packets per second. Monitoring unicast packets is crucial for assessing interface utilization and traffic load."
  },
  "ifOutUcastPkts": {
    "name": "Outgoing Unicast Packets Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing unicast packets over the past 5 minutes, measured in packets per second. By monitoring the number of unicast packets, administrators can assess the transmission performance of the interface and the usage of traffic."
  },
  "ifInOctets": {
    "name": "Interface Incoming Traffic Rate (per second)",
    "desc": "This metric indicates the average rate of bytes received over the past 5 minutes, converted to megabytes (MB). Monitoring byte traffic helps evaluate the load on the interface and bandwidth usage."
  },
  "ifOutOctets": {
    "name": "Interface Outgoing Traffic Rate (per second)",
    "desc": "This metric calculates the average rate of bytes sent over the past 5 minutes, measured in megabytes (MB). Monitoring outgoing traffic is crucial for ensuring data transmission quality and optimizing network performance."
  },
  "iftotalInOctets": {
    "name": "Device Total Incoming Traffic (per second)",
    "desc": "This metric indicates the average rate of total bytes received by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the incoming byte counts from multiple interfaces, this metric helps administrators obtain an overview of the device's incoming traffic, supporting overall traffic monitoring and capacity planning."
  },
  "iftotalOutOctets": {
    "name": "Device Total Outgoing Traffic (per second)",
    "desc": "This metric represents the average rate of total bytes sent by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the outgoing byte counts from multiple interfaces, this metric allows administrators to comprehensively assess the sending performance of the entire system, enabling more effective traffic management and optimization."
  }
},
    "Router": {
  "sysUpTime": {
    "name": "System Uptime",
    "desc": "This metric indicates the uptime of the device since the last restart, measured in days. By monitoring the uptime, network administrators can understand the stability and reliability of the device and identify potential reboot or failure issues."
  },
  "ifAdminStatus": {
    "name": "Interface Admin Status",
    "desc": "This metric indicates the administrative status of the network switch interface. It serves to indicate whether the interface is enabled (up) or disabled (down) by an administrator, along with other states such as testing or not present. This information is vital for network management and troubleshooting."
  },
  "ifOperStatus": {
    "name": "Interface Oper Status",
    "desc": "This metric reflects the actual operational status of the network switch interface, indicating whether the interface is operational. Unlike the administrative status, the operational status shows whether the interface can successfully receive and send traffic, which is crucial for monitoring network health."
  },
  "ifHighSpeed": {
    "name": "Interface Bandwidth",
    "desc": "This metric indicates the maximum data transmission speed supported by the network interface, usually measured in KB per second. Understanding the maximum speed of the interface helps administrators optimize traffic and utilize network resources effectively."
  },
  "ifInErrors": {
    "name": "Incoming Errors Rate (per second)",
    "desc": "This metric calculates the average rate of incoming error packets over the past 5 minutes, measured in packets per second. Monitoring incoming errors allows administrators to detect potential issues, such as physical connection faults or configuration errors, in a timely manner."
  },
  "ifOutErrors": {
    "name": "Outgoing Errors Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing error packets over the past 5 minutes, measured in packets per second. Monitoring outgoing errors is essential for identifying transmission issues and ensuring data integrity."
  },
  "ifInDiscards": {
    "name": "Incoming Discards Rate (per second)",
    "desc": "This metric represents the average rate of incoming discarded packets over the past 5 minutes, measured in packets per second. Packet discards may indicate network congestion or resource shortages, and monitoring this metric can help administrators optimize network performance."
  },
  "ifOutDiscards": {
    "name": "Outgoing Discards Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing discarded packets over the past 5 minutes, measured in packets per second. Monitoring outgoing discards can help identify network transmission issues and misconfigurations."
  },
  "ifInUcastPkts": {
    "name": "Incoming Unicast Packets Rate (per second)",
    "desc": "This metric indicates the average rate of incoming unicast packets over the past 5 minutes, measured in packets per second. Monitoring unicast packets is crucial for assessing interface utilization and traffic load."
  },
  "ifOutUcastPkts": {
    "name": "Outgoing Unicast Packets Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing unicast packets over the past 5 minutes, measured in packets per second. By monitoring the number of unicast packets, administrators can assess the transmission performance of the interface and the usage of traffic."
  },
  "ifInOctets": {
    "name": "Interface Incoming Traffic Rate (per second)",
    "desc": "This metric indicates the average rate of bytes received over the past 5 minutes, converted to megabytes (MB). Monitoring byte traffic helps evaluate the load on the interface and bandwidth usage."
  },
  "ifOutOctets": {
    "name": "Interface Outgoing Traffic Rate (per second)",
    "desc": "This metric calculates the average rate of bytes sent over the past 5 minutes, measured in megabytes (MB). Monitoring outgoing traffic is crucial for ensuring data transmission quality and optimizing network performance."
  },
  "iftotalInOctets": {
    "name": "Device Total Incoming Traffic (per second)",
    "desc": "This metric indicates the average rate of total bytes received by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the incoming byte counts from multiple interfaces, this metric helps administrators obtain an overview of the device's incoming traffic, supporting overall traffic monitoring and capacity planning."
  },
  "iftotalOutOctets": {
    "name": "Device Total Outgoing Traffic (per second)",
    "desc": "This metric represents the average rate of total bytes sent by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the outgoing byte counts from multiple interfaces, this metric allows administrators to comprehensively assess the sending performance of the entire system, enabling more effective traffic management and optimization."
  }
},
    "Loadbalance": {
  "sysUpTime": {
    "name": "System Uptime",
    "desc": "This metric indicates the uptime of the device since the last restart, measured in days. By monitoring the uptime, network administrators can understand the stability and reliability of the device and identify potential reboot or failure issues."
  },
  "ifAdminStatus": {
    "name": "Interface Admin Status",
    "desc": "This metric indicates the administrative status of the network switch interface. It serves to indicate whether the interface is enabled (up) or disabled (down) by an administrator, along with other states such as testing or not present. This information is vital for network management and troubleshooting."
  },
  "ifOperStatus": {
    "name": "Interface Oper Status",
    "desc": "This metric reflects the actual operational status of the network switch interface, indicating whether the interface is operational. Unlike the administrative status, the operational status shows whether the interface can successfully receive and send traffic, which is crucial for monitoring network health."
  },
  "ifHighSpeed": {
    "name": "Interface Bandwidth",
    "desc": "This metric indicates the maximum data transmission speed supported by the network interface, usually measured in KB per second. Understanding the maximum speed of the interface helps administrators optimize traffic and utilize network resources effectively."
  },
  "ifInErrors": {
    "name": "Incoming Errors Rate (per second)",
    "desc": "This metric calculates the average rate of incoming error packets over the past 5 minutes, measured in packets per second. Monitoring incoming errors allows administrators to detect potential issues, such as physical connection faults or configuration errors, in a timely manner."
  },
  "ifOutErrors": {
    "name": "Outgoing Errors Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing error packets over the past 5 minutes, measured in packets per second. Monitoring outgoing errors is essential for identifying transmission issues and ensuring data integrity."
  },
  "ifInDiscards": {
    "name": "Incoming Discards Rate (per second)",
    "desc": "This metric represents the average rate of incoming discarded packets over the past 5 minutes, measured in packets per second. Packet discards may indicate network congestion or resource shortages, and monitoring this metric can help administrators optimize network performance."
  },
  "ifOutDiscards": {
    "name": "Outgoing Discards Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing discarded packets over the past 5 minutes, measured in packets per second. Monitoring outgoing discards can help identify network transmission issues and misconfigurations."
  },
  "ifInUcastPkts": {
    "name": "Incoming Unicast Packets Rate (per second)",
    "desc": "This metric indicates the average rate of incoming unicast packets over the past 5 minutes, measured in packets per second. Monitoring unicast packets is crucial for assessing interface utilization and traffic load."
  },
  "ifOutUcastPkts": {
    "name": "Outgoing Unicast Packets Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing unicast packets over the past 5 minutes, measured in packets per second. By monitoring the number of unicast packets, administrators can assess the transmission performance of the interface and the usage of traffic."
  },
  "ifInOctets": {
    "name": "Interface Incoming Traffic Rate (per second)",
    "desc": "This metric indicates the average rate of bytes received over the past 5 minutes, converted to megabytes (MB). Monitoring byte traffic helps evaluate the load on the interface and bandwidth usage."
  },
  "ifOutOctets": {
    "name": "Interface Outgoing Traffic Rate (per second)",
    "desc": "This metric calculates the average rate of bytes sent over the past 5 minutes, measured in megabytes (MB). Monitoring outgoing traffic is crucial for ensuring data transmission quality and optimizing network performance."
  },
  "iftotalInOctets": {
    "name": "Device Total Incoming Traffic (per second)",
    "desc": "This metric indicates the average rate of total bytes received by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the incoming byte counts from multiple interfaces, this metric helps administrators obtain an overview of the device's incoming traffic, supporting overall traffic monitoring and capacity planning."
  },
  "iftotalOutOctets": {
    "name": "Device Total Outgoing Traffic (per second)",
    "desc": "This metric represents the average rate of total bytes sent by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the outgoing byte counts from multiple interfaces, this metric allows administrators to comprehensively assess the sending performance of the entire system, enabling more effective traffic management and optimization."
  }
},
    "Firewall": {
  "sysUpTime": {
    "name": "System Uptime",
    "desc": "This metric indicates the uptime of the device since the last restart, measured in days. By monitoring the uptime, network administrators can understand the stability and reliability of the device and identify potential reboot or failure issues."
  },
  "ifAdminStatus": {
    "name": "Interface Admin Status",
    "desc": "This metric indicates the administrative status of the network switch interface. It serves to indicate whether the interface is enabled (up) or disabled (down) by an administrator, along with other states such as testing or not present. This information is vital for network management and troubleshooting."
  },
  "ifOperStatus": {
    "name": "Interface Oper Status",
    "desc": "This metric reflects the actual operational status of the network switch interface, indicating whether the interface is operational. Unlike the administrative status, the operational status shows whether the interface can successfully receive and send traffic, which is crucial for monitoring network health."
  },
  "ifHighSpeed": {
    "name": "Interface Bandwidth",
    "desc": "This metric indicates the maximum data transmission speed supported by the network interface, usually measured in KB per second. Understanding the maximum speed of the interface helps administrators optimize traffic and utilize network resources effectively."
  },
  "ifInErrors": {
    "name": "Incoming Errors Rate (per second)",
    "desc": "This metric calculates the average rate of incoming error packets over the past 5 minutes, measured in packets per second. Monitoring incoming errors allows administrators to detect potential issues, such as physical connection faults or configuration errors, in a timely manner."
  },
  "ifOutErrors": {
    "name": "Outgoing Errors Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing error packets over the past 5 minutes, measured in packets per second. Monitoring outgoing errors is essential for identifying transmission issues and ensuring data integrity."
  },
  "ifInDiscards": {
    "name": "Incoming Discards Rate (per second)",
    "desc": "This metric represents the average rate of incoming discarded packets over the past 5 minutes, measured in packets per second. Packet discards may indicate network congestion or resource shortages, and monitoring this metric can help administrators optimize network performance."
  },
  "ifOutDiscards": {
    "name": "Outgoing Discards Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing discarded packets over the past 5 minutes, measured in packets per second. Monitoring outgoing discards can help identify network transmission issues and misconfigurations."
  },
  "ifInUcastPkts": {
    "name": "Incoming Unicast Packets Rate (per second)",
    "desc": "This metric indicates the average rate of incoming unicast packets over the past 5 minutes, measured in packets per second. Monitoring unicast packets is crucial for assessing interface utilization and traffic load."
  },
  "ifOutUcastPkts": {
    "name": "Outgoing Unicast Packets Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing unicast packets over the past 5 minutes, measured in packets per second. By monitoring the number of unicast packets, administrators can assess the transmission performance of the interface and the usage of traffic."
  },
  "ifInOctets": {
    "name": "Interface Incoming Traffic Rate (per second)",
    "desc": "This metric indicates the average rate of bytes received over the past 5 minutes, converted to megabytes (MB). Monitoring byte traffic helps evaluate the load on the interface and bandwidth usage."
  },
  "ifOutOctets": {
    "name": "Interface Outgoing Traffic Rate (per second)",
    "desc": "This metric calculates the average rate of bytes sent over the past 5 minutes, measured in megabytes (MB). Monitoring outgoing traffic is crucial for ensuring data transmission quality and optimizing network performance."
  },
  "iftotalInOctets": {
    "name": "Device Total Incoming Traffic (per second)",
    "desc": "This metric indicates the average rate of total bytes received by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the incoming byte counts from multiple interfaces, this metric helps administrators obtain an overview of the device's incoming traffic, supporting overall traffic monitoring and capacity planning."
  },
  "iftotalOutOctets": {
    "name": "Device Total Outgoing Traffic (per second)",
    "desc": "This metric represents the average rate of total bytes sent by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the outgoing byte counts from multiple interfaces, this metric allows administrators to comprehensively assess the sending performance of the entire system, enabling more effective traffic management and optimization."
  }
},
    "Detection Device": {
  "sysUpTime": {
    "name": "System Uptime",
    "desc": "This metric indicates the uptime of the device since the last restart, measured in days. By monitoring the uptime, network administrators can understand the stability and reliability of the device and identify potential reboot or failure issues."
  },
  "ifAdminStatus": {
    "name": "Interface Admin Status",
    "desc": "This metric indicates the administrative status of the network switch interface. It serves to indicate whether the interface is enabled (up) or disabled (down) by an administrator, along with other states such as testing or not present. This information is vital for network management and troubleshooting."
  },
  "ifOperStatus": {
    "name": "Interface Oper Status",
    "desc": "This metric reflects the actual operational status of the network switch interface, indicating whether the interface is operational. Unlike the administrative status, the operational status shows whether the interface can successfully receive and send traffic, which is crucial for monitoring network health."
  },
  "ifHighSpeed": {
    "name": "Interface Bandwidth",
    "desc": "This metric indicates the maximum data transmission speed supported by the network interface, usually measured in KB per second. Understanding the maximum speed of the interface helps administrators optimize traffic and utilize network resources effectively."
  },
  "ifInErrors": {
    "name": "Incoming Errors Rate (per second)",
    "desc": "This metric calculates the average rate of incoming error packets over the past 5 minutes, measured in packets per second. Monitoring incoming errors allows administrators to detect potential issues, such as physical connection faults or configuration errors, in a timely manner."
  },
  "ifOutErrors": {
    "name": "Outgoing Errors Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing error packets over the past 5 minutes, measured in packets per second. Monitoring outgoing errors is essential for identifying transmission issues and ensuring data integrity."
  },
  "ifInDiscards": {
    "name": "Incoming Discards Rate (per second)",
    "desc": "This metric represents the average rate of incoming discarded packets over the past 5 minutes, measured in packets per second. Packet discards may indicate network congestion or resource shortages, and monitoring this metric can help administrators optimize network performance."
  },
  "ifOutDiscards": {
    "name": "Outgoing Discards Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing discarded packets over the past 5 minutes, measured in packets per second. Monitoring outgoing discards can help identify network transmission issues and misconfigurations."
  },
  "ifInUcastPkts": {
    "name": "Incoming Unicast Packets Rate (per second)",
    "desc": "This metric indicates the average rate of incoming unicast packets over the past 5 minutes, measured in packets per second. Monitoring unicast packets is crucial for assessing interface utilization and traffic load."
  },
  "ifOutUcastPkts": {
    "name": "Outgoing Unicast Packets Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing unicast packets over the past 5 minutes, measured in packets per second. By monitoring the number of unicast packets, administrators can assess the transmission performance of the interface and the usage of traffic."
  },
  "ifInOctets": {
    "name": "Interface Incoming Traffic Rate (per second)",
    "desc": "This metric indicates the average rate of bytes received over the past 5 minutes, converted to megabytes (MB). Monitoring byte traffic helps evaluate the load on the interface and bandwidth usage."
  },
  "ifOutOctets": {
    "name": "Interface Outgoing Traffic Rate (per second)",
    "desc": "This metric calculates the average rate of bytes sent over the past 5 minutes, measured in megabytes (MB). Monitoring outgoing traffic is crucial for ensuring data transmission quality and optimizing network performance."
  },
  "iftotalInOctets": {
    "name": "Device Total Incoming Traffic (per second)",
    "desc": "This metric indicates the average rate of total bytes received by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the incoming byte counts from multiple interfaces, this metric helps administrators obtain an overview of the device's incoming traffic, supporting overall traffic monitoring and capacity planning."
  },
  "iftotalOutOctets": {
    "name": "Device Total Outgoing Traffic (per second)",
    "desc": "This metric represents the average rate of total bytes sent by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the outgoing byte counts from multiple interfaces, this metric allows administrators to comprehensively assess the sending performance of the entire system, enabling more effective traffic management and optimization."
  }
},
    "Bastion Host": {
  "sysUpTime": {
    "name": "System Uptime",
    "desc": "This metric indicates the uptime of the device since the last restart, measured in days. By monitoring the uptime, network administrators can understand the stability and reliability of the device and identify potential reboot or failure issues."
  },
  "ifAdminStatus": {
    "name": "Interface Admin Status",
    "desc": "This metric indicates the administrative status of the network switch interface. It serves to indicate whether the interface is enabled (up) or disabled (down) by an administrator, along with other states such as testing or not present. This information is vital for network management and troubleshooting."
  },
  "ifOperStatus": {
    "name": "Interface Oper Status",
    "desc": "This metric reflects the actual operational status of the network switch interface, indicating whether the interface is operational. Unlike the administrative status, the operational status shows whether the interface can successfully receive and send traffic, which is crucial for monitoring network health."
  },
  "ifHighSpeed": {
    "name": "Interface Bandwidth",
    "desc": "This metric indicates the maximum data transmission speed supported by the network interface, usually measured in KB per second. Understanding the maximum speed of the interface helps administrators optimize traffic and utilize network resources effectively."
  },
  "ifInErrors": {
    "name": "Incoming Errors Rate (per second)",
    "desc": "This metric calculates the average rate of incoming error packets over the past 5 minutes, measured in packets per second. Monitoring incoming errors allows administrators to detect potential issues, such as physical connection faults or configuration errors, in a timely manner."
  },
  "ifOutErrors": {
    "name": "Outgoing Errors Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing error packets over the past 5 minutes, measured in packets per second. Monitoring outgoing errors is essential for identifying transmission issues and ensuring data integrity."
  },
  "ifInDiscards": {
    "name": "Incoming Discards Rate (per second)",
    "desc": "This metric represents the average rate of incoming discarded packets over the past 5 minutes, measured in packets per second. Packet discards may indicate network congestion or resource shortages, and monitoring this metric can help administrators optimize network performance."
  },
  "ifOutDiscards": {
    "name": "Outgoing Discards Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing discarded packets over the past 5 minutes, measured in packets per second. Monitoring outgoing discards can help identify network transmission issues and misconfigurations."
  },
  "ifInUcastPkts": {
    "name": "Incoming Unicast Packets Rate (per second)",
    "desc": "This metric indicates the average rate of incoming unicast packets over the past 5 minutes, measured in packets per second. Monitoring unicast packets is crucial for assessing interface utilization and traffic load."
  },
  "ifOutUcastPkts": {
    "name": "Outgoing Unicast Packets Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing unicast packets over the past 5 minutes, measured in packets per second. By monitoring the number of unicast packets, administrators can assess the transmission performance of the interface and the usage of traffic."
  },
  "ifInOctets": {
    "name": "Interface Incoming Traffic Rate (per second)",
    "desc": "This metric indicates the average rate of bytes received over the past 5 minutes, converted to megabytes (MB). Monitoring byte traffic helps evaluate the load on the interface and bandwidth usage."
  },
  "ifOutOctets": {
    "name": "Interface Outgoing Traffic Rate (per second)",
    "desc": "This metric calculates the average rate of bytes sent over the past 5 minutes, measured in megabytes (MB). Monitoring outgoing traffic is crucial for ensuring data transmission quality and optimizing network performance."
  },
  "iftotalInOctets": {
    "name": "Device Total Incoming Traffic (per second)",
    "desc": "This metric indicates the average rate of total bytes received by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the incoming byte counts from multiple interfaces, this metric helps administrators obtain an overview of the device's incoming traffic, supporting overall traffic monitoring and capacity planning."
  },
  "iftotalOutOctets": {
    "name": "Device Total Outgoing Traffic (per second)",
    "desc": "This metric represents the average rate of total bytes sent by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the outgoing byte counts from multiple interfaces, this metric allows administrators to comprehensively assess the sending performance of the entire system, enabling more effective traffic management and optimization."
  }
},
    "Scanning Device": {
  "sysUpTime": {
    "name": "System Uptime",
    "desc": "This metric indicates the uptime of the device since the last restart, measured in days. By monitoring the uptime, network administrators can understand the stability and reliability of the device and identify potential reboot or failure issues."
  },
  "ifAdminStatus": {
    "name": "Interface Admin Status",
    "desc": "This metric indicates the administrative status of the network switch interface. It serves to indicate whether the interface is enabled (up) or disabled (down) by an administrator, along with other states such as testing or not present. This information is vital for network management and troubleshooting."
  },
  "ifOperStatus": {
    "name": "Interface Oper Status",
    "desc": "This metric reflects the actual operational status of the network switch interface, indicating whether the interface is operational. Unlike the administrative status, the operational status shows whether the interface can successfully receive and send traffic, which is crucial for monitoring network health."
  },
  "ifHighSpeed": {
    "name": "Interface Bandwidth",
    "desc": "This metric indicates the maximum data transmission speed supported by the network interface, usually measured in KB per second. Understanding the maximum speed of the interface helps administrators optimize traffic and utilize network resources effectively."
  },
  "ifInErrors": {
    "name": "Incoming Errors Rate (per second)",
    "desc": "This metric calculates the average rate of incoming error packets over the past 5 minutes, measured in packets per second. Monitoring incoming errors allows administrators to detect potential issues, such as physical connection faults or configuration errors, in a timely manner."
  },
  "ifOutErrors": {
    "name": "Outgoing Errors Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing error packets over the past 5 minutes, measured in packets per second. Monitoring outgoing errors is essential for identifying transmission issues and ensuring data integrity."
  },
  "ifInDiscards": {
    "name": "Incoming Discards Rate (per second)",
    "desc": "This metric represents the average rate of incoming discarded packets over the past 5 minutes, measured in packets per second. Packet discards may indicate network congestion or resource shortages, and monitoring this metric can help administrators optimize network performance."
  },
  "ifOutDiscards": {
    "name": "Outgoing Discards Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing discarded packets over the past 5 minutes, measured in packets per second. Monitoring outgoing discards can help identify network transmission issues and misconfigurations."
  },
  "ifInUcastPkts": {
    "name": "Incoming Unicast Packets Rate (per second)",
    "desc": "This metric indicates the average rate of incoming unicast packets over the past 5 minutes, measured in packets per second. Monitoring unicast packets is crucial for assessing interface utilization and traffic load."
  },
  "ifOutUcastPkts": {
    "name": "Outgoing Unicast Packets Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing unicast packets over the past 5 minutes, measured in packets per second. By monitoring the number of unicast packets, administrators can assess the transmission performance of the interface and the usage of traffic."
  },
  "ifInOctets": {
    "name": "Interface Incoming Traffic Rate (per second)",
    "desc": "This metric indicates the average rate of bytes received over the past 5 minutes, converted to megabytes (MB). Monitoring byte traffic helps evaluate the load on the interface and bandwidth usage."
  },
  "ifOutOctets": {
    "name": "Interface Outgoing Traffic Rate (per second)",
    "desc": "This metric calculates the average rate of bytes sent over the past 5 minutes, measured in megabytes (MB). Monitoring outgoing traffic is crucial for ensuring data transmission quality and optimizing network performance."
  },
  "iftotalInOctets": {
    "name": "Device Total Incoming Traffic (per second)",
    "desc": "This metric indicates the average rate of total bytes received by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the incoming byte counts from multiple interfaces, this metric helps administrators obtain an overview of the device's incoming traffic, supporting overall traffic monitoring and capacity planning."
  },
  "iftotalOutOctets": {
    "name": "Device Total Outgoing Traffic (per second)",
    "desc": "This metric represents the average rate of total bytes sent by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the outgoing byte counts from multiple interfaces, this metric allows administrators to comprehensively assess the sending performance of the entire system, enabling more effective traffic management and optimization."
  }
},
    "Storage": {
    "sysUpTime": {
    "name": "System Uptime",
    "desc": "This metric indicates the uptime of the device since the last restart, measured in days. By monitoring the uptime, network administrators can understand the stability and reliability of the device and identify potential reboot or failure issues."
  },
  "ifAdminStatus": {
    "name": "Interface Admin Status",
    "desc": "This metric indicates the administrative status of the network switch interface. It serves to indicate whether the interface is enabled (up) or disabled (down) by an administrator, along with other states such as testing or not present. This information is vital for network management and troubleshooting."
  },
  "ifOperStatus": {
    "name": "Interface Oper Status",
    "desc": "This metric reflects the actual operational status of the network switch interface, indicating whether the interface is operational. Unlike the administrative status, the operational status shows whether the interface can successfully receive and send traffic, which is crucial for monitoring network health."
  },
  "ifHighSpeed": {
    "name": "Interface Bandwidth",
    "desc": "This metric indicates the maximum data transmission speed supported by the network interface, usually measured in KB per second. Understanding the maximum speed of the interface helps administrators optimize traffic and utilize network resources effectively."
  },
  "ifInErrors": {
    "name": "Incoming Errors Rate (per second)",
    "desc": "This metric calculates the average rate of incoming error packets over the past 5 minutes, measured in packets per second. Monitoring incoming errors allows administrators to detect potential issues, such as physical connection faults or configuration errors, in a timely manner."
  },
  "ifOutErrors": {
    "name": "Outgoing Errors Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing error packets over the past 5 minutes, measured in packets per second. Monitoring outgoing errors is essential for identifying transmission issues and ensuring data integrity."
  },
  "ifInDiscards": {
    "name": "Incoming Discards Rate (per second)",
    "desc": "This metric represents the average rate of incoming discarded packets over the past 5 minutes, measured in packets per second. Packet discards may indicate network congestion or resource shortages, and monitoring this metric can help administrators optimize network performance."
  },
  "ifOutDiscards": {
    "name": "Outgoing Discards Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing discarded packets over the past 5 minutes, measured in packets per second. Monitoring outgoing discards can help identify network transmission issues and misconfigurations."
  },
  "ifInUcastPkts": {
    "name": "Incoming Unicast Packets Rate (per second)",
    "desc": "This metric indicates the average rate of incoming unicast packets over the past 5 minutes, measured in packets per second. Monitoring unicast packets is crucial for assessing interface utilization and traffic load."
  },
  "ifOutUcastPkts": {
    "name": "Outgoing Unicast Packets Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing unicast packets over the past 5 minutes, measured in packets per second. By monitoring the number of unicast packets, administrators can assess the transmission performance of the interface and the usage of traffic."
  },
  "ifInOctets": {
    "name": "Interface Incoming Traffic Rate (per second)",
    "desc": "This metric indicates the average rate of bytes received over the past 5 minutes, converted to megabytes (MB). Monitoring byte traffic helps evaluate the load on the interface and bandwidth usage."
  },
  "ifOutOctets": {
    "name": "Interface Outgoing Traffic Rate (per second)",
    "desc": "This metric calculates the average rate of bytes sent over the past 5 minutes, measured in megabytes (MB). Monitoring outgoing traffic is crucial for ensuring data transmission quality and optimizing network performance."
  },
  "iftotalInOctets": {
    "name": "Device Total Incoming Traffic (per second)",
    "desc": "This metric indicates the average rate of total bytes received by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the incoming byte counts from multiple interfaces, this metric helps administrators obtain an overview of the device's incoming traffic, supporting overall traffic monitoring and capacity planning."
  },
  "iftotalOutOctets": {
    "name": "Device Total Outgoing Traffic (per second)",
    "desc": "This metric represents the average rate of total bytes sent by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the outgoing byte counts from multiple interfaces, this metric allows administrators to comprehensively assess the sending performance of the entire system, enabling more effective traffic management and optimization."
  },"ipmi_chassis_power_state": {
        "name": "Power State",
        "desc": "The power state indicator is used to monitor if the device is powered on. Its value can indicate whether the power is on or off. It is mainly used for remote management and monitoring of the device's power state."
    },
    "ipmi_power_watts": {
        "name": "Power",
        "desc": "The power indicator is measured in watts and reflects the current power consumption of the device. This indicator helps evaluate the device's energy efficiency and power consumption trends. It facilitates the implementation of energy-saving policies and resource optimization."
    },
    "ipmi_voltage_volts": {
        "name": "Voltage",
        "desc": "The voltage indicator measured in volts monitors the voltage levels of different power rails within the device. Stable voltage supply is crucial for the reliability of the device. This indicator helps quickly identify electrical issues, ensuring normal operation."
    },
    "ipmi_fan_speed_rpm": {
        "name": "Fan Speed",
        "desc": "The fan speed indicator is measured in rotations per minute (rpm) and monitors the fan's operation status within the device. Efficient fan operation is key to maintaining device temperature. It helps prevent overheating and ensures the device's stable long-term operation."
    },
    "ipmi_temperature_celsius": {
        "name": "Temperature",
        "desc": "The temperature indicator measured in degrees Celsius monitors the internal temperature of the device. Monitoring temperature prevents heat accumulation and avoids device overheating. It is crucial for maintaining system stability and longevity."
    }
    },
    "Hardware Server": {
 "sysUpTime": {
    "name": "System Uptime",
    "desc": "This metric indicates the uptime of the device since the last restart, measured in days. By monitoring the uptime, network administrators can understand the stability and reliability of the device and identify potential reboot or failure issues."
  },
  "ifAdminStatus": {
    "name": "Interface Admin Status",
    "desc": "This metric indicates the administrative status of the network switch interface. It serves to indicate whether the interface is enabled (up) or disabled (down) by an administrator, along with other states such as testing or not present. This information is vital for network management and troubleshooting."
  },
  "ifOperStatus": {
    "name": "Interface Oper Status",
    "desc": "This metric reflects the actual operational status of the network switch interface, indicating whether the interface is operational. Unlike the administrative status, the operational status shows whether the interface can successfully receive and send traffic, which is crucial for monitoring network health."
  },
  "ifHighSpeed": {
    "name": "Interface Bandwidth",
    "desc": "This metric indicates the maximum data transmission speed supported by the network interface, usually measured in KB per second. Understanding the maximum speed of the interface helps administrators optimize traffic and utilize network resources effectively."
  },
  "ifInErrors": {
    "name": "Incoming Errors Rate (per second)",
    "desc": "This metric calculates the average rate of incoming error packets over the past 5 minutes, measured in packets per second. Monitoring incoming errors allows administrators to detect potential issues, such as physical connection faults or configuration errors, in a timely manner."
  },
  "ifOutErrors": {
    "name": "Outgoing Errors Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing error packets over the past 5 minutes, measured in packets per second. Monitoring outgoing errors is essential for identifying transmission issues and ensuring data integrity."
  },
  "ifInDiscards": {
    "name": "Incoming Discards Rate (per second)",
    "desc": "This metric represents the average rate of incoming discarded packets over the past 5 minutes, measured in packets per second. Packet discards may indicate network congestion or resource shortages, and monitoring this metric can help administrators optimize network performance."
  },
  "ifOutDiscards": {
    "name": "Outgoing Discards Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing discarded packets over the past 5 minutes, measured in packets per second. Monitoring outgoing discards can help identify network transmission issues and misconfigurations."
  },
  "ifInUcastPkts": {
    "name": "Incoming Unicast Packets Rate (per second)",
    "desc": "This metric indicates the average rate of incoming unicast packets over the past 5 minutes, measured in packets per second. Monitoring unicast packets is crucial for assessing interface utilization and traffic load."
  },
  "ifOutUcastPkts": {
    "name": "Outgoing Unicast Packets Rate (per second)",
    "desc": "This metric calculates the average rate of outgoing unicast packets over the past 5 minutes, measured in packets per second. By monitoring the number of unicast packets, administrators can assess the transmission performance of the interface and the usage of traffic."
  },
  "ifInOctets": {
    "name": "Interface Incoming Traffic Rate (per second)",
    "desc": "This metric indicates the average rate of bytes received over the past 5 minutes, converted to megabytes (MB). Monitoring byte traffic helps evaluate the load on the interface and bandwidth usage."
  },
  "ifOutOctets": {
    "name": "Interface Outgoing Traffic Rate (per second)",
    "desc": "This metric calculates the average rate of bytes sent over the past 5 minutes, measured in megabytes (MB). Monitoring outgoing traffic is crucial for ensuring data transmission quality and optimizing network performance."
  },
  "iftotalInOctets": {
    "name": "Device Total Incoming Traffic (per second)",
    "desc": "This metric indicates the average rate of total bytes received by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the incoming byte counts from multiple interfaces, this metric helps administrators obtain an overview of the device's incoming traffic, supporting overall traffic monitoring and capacity planning."
  },
  "iftotalOutOctets": {
    "name": "Device Total Outgoing Traffic (per second)",
    "desc": "This metric represents the average rate of total bytes sent by the entire device over the past 5 minutes, measured in megabytes per second (MB/s). By summing the outgoing byte counts from multiple interfaces, this metric allows administrators to comprehensively assess the sending performance of the entire system, enabling more effective traffic management and optimization."
  },"ipmi_chassis_power_state": {
        "name": "Power State",
        "desc": "The power state indicator is used to monitor if the device is powered on. Its value can indicate whether the power is on or off. It is mainly used for remote management and monitoring of the device's power state."
    },
    "ipmi_power_watts": {
        "name": "Power",
        "desc": "The power indicator is measured in watts and reflects the current power consumption of the device. This indicator helps evaluate the device's energy efficiency and power consumption trends. It facilitates the implementation of energy-saving policies and resource optimization."
    },
    "ipmi_voltage_volts": {
        "name": "Voltage",
        "desc": "The voltage indicator measured in volts monitors the voltage levels of different power rails within the device. Stable voltage supply is crucial for the reliability of the device. This indicator helps quickly identify electrical issues, ensuring normal operation."
    },
    "ipmi_fan_speed_rpm": {
        "name": "Fan Speed",
        "desc": "The fan speed indicator is measured in rotations per minute (rpm) and monitors the fan's operation status within the device. Efficient fan operation is key to maintaining device temperature. It helps prevent overheating and ensures the device's stable long-term operation."
    },
    "ipmi_temperature_celsius": {
        "name": "Temperature",
        "desc": "The temperature indicator measured in degrees Celsius monitors the internal temperature of the device. Monitoring temperature prevents heat accumulation and avoids device overheating. It is crucial for maintaining system stability and longevity."
    }
},
    "SNMP Trap": {                     
    },
    "Zookeeper": {
    "zookeeper_uptime": {
        "name": "Uptime",
        "desc": "This metric shows the uptime of the Zookeeper service, helping to monitor if the system is running normally."
    },
    "zookeeper_avg_latency": {
        "name": "Average Latency",
        "desc": "This metric represents the average latency of Zookeeper processing requests, used to monitor system response capability."
    },
    "zookeeper_read_write_ratio": {
        "name": "Read/Write Ratio",
        "desc": "This metric represents the ratio of commits to snapshots in Zookeeper, helping to assess the read/write load distribution."
    },
    "zookeeper_snapshot_to_commit_ratio": {
        "name": "Snapshot to Commit Ratio",
        "desc": "This metric represents the ratio of snapshot generation frequency to commit request frequency in Zookeeper, helping to monitor the relationship between persistence operations and transaction commits."
    },
    "zookeeper_connection_drop_count": {
        "name": "Connection Drop Count",
        "desc": "This metric represents the number of connection drops in Zookeeper, used to monitor connection stability."
    },
    "zookeeper_connection_rejected": {
        "name": "Connection Rejected",
        "desc": "This metric represents the number of rejected connections in Zookeeper, helping to monitor if connections are being correctly handled."
    },
    "zookeeper_znode_count": {
        "name": "Znode Count",
        "desc": "This metric represents the number of znodes in Zookeeper, helping to monitor changes in Zookeeper's data size."
    },
    "zookeeper_packets_received": {
        "name": "Packets Received",
        "desc": "This metric shows the number of packets received by Zookeeper, helping to monitor the network traffic."
    }
},
"Apache": {
    "apache_uptime": {
        "name": "Uptime",
        "desc": "This metric represents the uptime of the Apache server since it was started, used to monitor the server's health."
    },
    "apache_busy_workers": {
        "name": "Busy Workers",
        "desc": "This metric represents the number of busy worker processes in the Apache server, used to assess the server's load."
    },
    "apache_idle_workers": {
        "name": "Idle Workers",
        "desc": "This metric represents the number of idle worker processes in the Apache server, reflecting the server's resource utilization."
    },
    "apache_req_per_sec": {
        "name": "Requests per Second",
        "desc": "This metric represents the number of requests handled by Apache per second, used to monitor the server's request processing capability."
    },
    "apache_bytes_per_sec": {
        "name": "Bytes per Second",
        "desc": "This metric represents the number of bytes transferred by Apache per second, reflecting the network traffic."
    },
    "apache_total_accesses": {
        "name": "Total Accesses",
        "desc": "This metric represents the total number of accesses to the Apache server since startup, reflecting the overall request volume."
    },
    "apache_total_duration": {
        "name": "Total Duration",
        "desc": "This metric represents the total request processing duration since the Apache server started, used to assess the server's processing load."
    },
    "apache_cpu_system": {
        "name": "System CPU Usage",
        "desc": "This metric represents the CPU usage at the system level for Apache server."
    },
    "apache_cpu_user": {
        "name": "User CPU Usage",
        "desc": "This metric represents the CPU usage at the user process level for Apache server."
    },
    "apache_cpu_load": {
        "name": "CPU Load",
        "desc": "This metric represents the CPU load of the Apache server, reflecting the overall load of the system."
    },
    "apache_duration_per_req": {
        "name": "Duration per Request",
        "desc": "This metric represents the average duration per request, helping to evaluate the efficiency of request handling by the server."
    }
},
"ClickHouse": {
    "clickhouse_asynchronous_metrics_uptime": {
        "name": "Uptime",
        "desc": "Represents the uptime of the ClickHouse system."
    },
    "clickhouse_metrics_memory_tracking": {
        "name": "Memory Tracking",
        "desc": "Indicates the current memory usage by the ClickHouse process."
    },
    "clickhouse_asynchronous_metrics_os_memory_available": {
        "name": "Available Memory",
        "desc": "Indicates the total physical memory available for processes."
    },
    "clickhouse_asynchronous_metrics_disk_used_default": {
        "name": "Disk Usage (Default)",
        "desc": "Represents the amount of disk space currently used on the default disk."
    },
    "clickhouse_asynchronous_metrics_disk_total_default": {
        "name": "Total Disk Capacity (Default)",
        "desc": "Displays the total capacity of the default disk."
    },
    "clickhouse_events_query": {
        "name": "Query Rate",
        "desc": "Displays the number of queries processed per second by ClickHouse."
    },
    "clickhouse_events_inserted_rows": {
        "name": "Inserted Rows Rate",
        "desc": "Represents the rate of rows inserted during the last 5 minutes."
    },
    "clickhouse_events_select_query": {
        "name": "Select Query Rate",
        "desc": "Represents the rate of SELECT queries processed during the last 5 minutes."
    },
    "clickhouse_events_compressed_read_buffer_bytes": {
        "name": "Compressed Data Read Rate",
        "desc": "Displays the rate of compressed data read by ClickHouse system, indicating IO performance."
    },
    "clickhouse_metrics_parts_active": {
        "name": "Active Parts Count",
        "desc": "Displays the number of active parts in the MergeTree tables."
    },
    "clickhouse_metrics_parts_outdated": {
        "name": "Outdated Parts Count",
        "desc": "Shows the count of outdated parts in the MergeTree tables."
    },
    "clickhouse_asynchronous_metrics_load_average1": {
        "name": "Load Average (1m)",
        "desc": "Indicates the average system load over the last 1 minute."
    }
},
"RabbitMQ": {
    "rabbitmq_exchange_publish_in_rate": {
        "name": "Exchange Publish In Rate",
        "desc": "This metric shows the rate of messages published to the RabbitMQ exchange per second. It helps identify bottlenecks in message inflow."
    },
    "rabbitmq_exchange_publish_out_rate": {
        "name": "Exchange Publish Out Rate",
        "desc": "This metric shows the rate of messages published out of the RabbitMQ exchange per second. It helps identify issues in message outflow."
    },
    "rabbitmq_node_disk_free": {
        "name": "Disk Space Free",
        "desc": "This metric indicates the free disk space on the RabbitMQ node, in bytes. Low disk space can lead to performance degradation or failures."
    },
    "rabbitmq_node_fd_used": {
        "name": "File Descriptors Used",
        "desc": "This metric shows the number of file descriptors used by the RabbitMQ node. Excessive use may prevent the system from handling additional connections."
    },
    "rabbitmq_node_mem_used": {
        "name": "Memory Used",
        "desc": "This metric indicates the memory usage on the RabbitMQ node. High memory usage may lead to performance issues or node crashes."
    },
    "rabbitmq_node_run_queue": {
        "name": "Run Queue",
        "desc": "This metric shows the number of queues currently being handled by the RabbitMQ node. A high number may indicate system pressure and need for optimization."
    },
    "rabbitmq_node_uptime": {
        "name": "Uptime",
        "desc": "This metric indicates the uptime of the RabbitMQ node, in seconds. Nodes running for extended periods may require a restart to free resources and perform maintenance."
    },
    "rabbitmq_fd_usage_ratio": {
        "name": "File Descriptor Usage Ratio",
        "desc": "This metric shows the ratio of used file descriptors to the total number of file descriptors on the RabbitMQ node."
    },
    "rabbitmq_overview_messages_ready": {
        "name": "Messages Ready",
        "desc": "This metric indicates the number of messages ready for processing. A high number of ready messages may indicate consumer lag or slow processing speed."
    },
    "rabbitmq_overview_messages_unacked": {
        "name": "Unacknowledged Messages",
        "desc": "This metric represents the number of unacknowledged messages. A high number of unacknowledged messages may indicate slow consumer processing or backlog."
    },
    "rabbitmq_queue_message_backlog_ratio": {
        "name": "Queue Message Backlog Ratio",
        "desc": "This metric shows the ratio of ready messages to acked messages in the queue, helping to identify message backlog in the system."
    },
    "rabbitmq_unacked_message_ratio": {
        "name": "Unacked Message Ratio",
        "desc": "This metric shows the ratio of unacknowledged messages to the total messages in the queue, helping to identify slow consumers."
    }
},
"ActiveMQ": {
    "activemq_topic_consumer_count": {
        "name": "Consumer Count",
        "desc": "This metric represents the number of consumers per topic, used to monitor if consumers are evenly distributed."
    },
    "activemq_topic_dequeue_rate": {
        "name": "Dequeue Rate",
        "desc": "This metric shows the rate at which messages are consumed from the topic, indicating the consumption rate per second."
    },
    "activemq_topic_enqueue_rate": {
        "name": "Enqueue Rate",
        "desc": "This metric shows the rate at which messages are enqueued to the topic, indicating the incoming message rate per second."
    },
    "activemq_topic_size": {
        "name": "Topic Size",
        "desc": "This metric shows the number of unconsumed messages in the topic, helping to identify potential message backlog."
    }
},
"Nginx": {
    "nginx_requests": {
        "name": "Requests Rate",
        "desc": "Indicates the number of HTTP requests per second processed over the last 5 minutes, reflecting server load."
    },
    "nginx_accepts": {
        "name": "Accepted Connections Rate",
        "desc": "Indicates the number of client connections successfully established per second over the last 5 minutes, used to monitor connection activity."
    },
    "nginx_handled": {
        "name": "Handled Connections Rate",
        "desc": "Indicates the number of connected sessions successfully handled per second over the last 5 minutes, monitoring connection handling capacity."
    },
    "nginx_active": {
        "name": "Active Connections",
        "desc": "The number of active connections currently including those in reading, writing, and waiting states."
    },
    "nginx_waiting": {
        "name": "Waiting Connections",
        "desc": "The current number of idle connections waiting to be processed, reflecting the waiting connection queue."
    },
    "nginx_reading": {
        "name": "Reading Connections",
        "desc": "The number of connections currently reading client requests (header or body), used to monitor load in the reading stage."
    },
    "nginx_writing": {
        "name": "Writing Connections",
        "desc": "The number of connections currently writing response data to clients, used to monitor performance in the response stage."
    },
    "nginx_connect_rate": {
        "name": "Connection Handling Success Rate",
        "desc": "The percentage of handled connections out of total accepted connections over the last 5 minutes, used to analyze connection handling stability."
    },
    "nginx_request_handling_efficiency": {
        "name": "Requests per Handled Connection",
        "desc": "Indicates the average number of requests per handled connection, indirectly reflecting Nginx's efficiency and load level."
    }
},
"Tomcat": {
    "tomcat_connector_request_count": {
        "name": "Request Count",
        "desc": "This metric represents the total number of requests processed per second on average by the Tomcat connector in the past 5 minutes, and is used to monitor the request load."
    },
    "tomcat_connector_processing_time": {
        "name": "Processing Time",
        "desc": "This metric is used to measure the average per - second change in the time taken by the Tomcat connector to process requests over the past 5 minutes. It can reflect the efficiency of the server in processing requests."
    },
    "tomcat_connector_max_time": {
        "name": "Max Processing Time",
        "desc": "This metric indicates the maximum time taken to process a single request in Tomcat, reflecting the performance of the slowest request."
    },
    "tomcat_connector_bytes_received": {
        "name": "Bytes Received",
        "desc": "It represents the number of bytes of data received per second on average by the Tomcat connector in the past 5 minutes. It can be used to monitor the network traffic load of the Tomcat server."
    },
    "tomcat_connector_bytes_sent": {
        "name": "Bytes Sent",
        "desc": "This metric represents the average number of bytes sent per second by the Tomcat connector in the past 5 minutes, and it is used to monitor traffic and response load."
    },
    "tomcat_connector_current_thread_count": {
        "name": "Current Thread Count",
        "desc": "This metric shows the current number of threads used by the Tomcat connector, used to monitor concurrency capabilities."
    },
    "tomcat_connector_current_threads_busy": {
        "name": "Busy Thread Count",
        "desc": "This metric indicates the number of busy threads in the Tomcat connector, used to monitor concurrent processing."
    },
    "tomcat_connector_max_threads": {
        "name": "Max Thread Count",
        "desc": "This metric indicates the maximum number of threads for the Tomcat connector, used to monitor Tomcat's concurrency capabilities."
    },
    "tomcat_connector_error_count": {
        "name": "Error Count",
        "desc": "This metric represents the average number of errors per second that occur when the Tomcat connector processes requests in the past 5 minutes, and it is used to monitor the error rate."
    },
    "tomcat_jvm_memory_free": {
        "name": "JMX Free Memory",
        "desc": "This metric shows the free memory in Tomcat JVM, used to monitor memory usage."
    },
    "tomcat_jvm_memory_max": {
        "name": "JMX Max Memory",
        "desc": "This metric indicates the maximum memory available to Tomcat JVM, used to monitor memory limits."
    },
    "tomcat_jvm_memorypool_used": {
        "name": "JMX Used Memory Pool",
        "desc": "This metric shows the amount of memory used in the Tomcat JVM memory pool, used to monitor memory pool usage."
    }
},
"Consul": {
    "consul_health_checks_status": {
        "name": "Health Check Status",
        "desc": "This metric represents the status of the health check in Consul, where 0=passing, 1=warning, 2=critical."
    },
    "consul_health_checks_passing": {
        "name": "Passing Health Checks",
        "desc": "This metric indicates the number of passing health checks, used to monitor the health status of services."
    },
    "consul_health_checks_warning": {
        "name": "Warning Health Checks",
        "desc": "This metric shows the number of health checks in warning status, used to monitor potential issues."
    },
    "consul_health_checks_critical": {
        "name": "Critical Health Checks",
        "desc": "This metric shows the number of health checks in critical status, used to monitor critical failures."
    }
},
"ElasticSearch": {
    "elasticsearch_fs_total_available_in_bytes": {
        "name": "Total Available Disk Space",
        "desc": "Indicates total available disk space, converted to GB."
    },
    "elasticsearch_fs_total_free_in_bytes": {
        "name": "Total Free Disk Space",
        "desc": "Represents unallocated available disk space."
    },
    "elasticsearch_http_current_open": {
        "name": "Current Open HTTP Connections",
        "desc": "Tracks the number of currently open HTTP connections."
    },
    "elasticsearch_http_total_opened": {
        "name": "New HTTP Connections in 5m",
        "desc": "Number of new HTTP connections opened in 5 minutes."
    },
    "elasticsearch_fs_io_stats_total_write_kilobytes": {
        "name": "Disk Write Throughput",
        "desc": "Monitors disk write throughput (MB/s)."
    },
    "elasticsearch_fs_io_stats_total_read_kilobytes": {
        "name": "Disk Read Throughput",
        "desc": "Tracks disk read throughput (MB/s)."
    },
    "elasticsearch_indices_docs_count": {
        "name": "Total Document Count",
        "desc": "Total number of document entries in Elasticsearch."
    },
    "elasticsearch_indices_docs_deleted": {
        "name": "Total Deleted Document Count",
        "desc": "Total number of deleted documents in Elasticsearch."
    },
    "elasticsearch_indices_query_cache_cache_count": {
        "name": "Query Cache Count",
        "desc": "Tracks the number of query cache entries."
    },
    "elasticsearch_breakers_parent_tripped": {
        "name": "Parent Circuit Breaker Tripped",
        "desc": "Parent circuit breaker trips in 5 minutes."
    },
    "elasticsearch_breakers_fielddata_tripped": {
        "name": "Field Data Circuit Breaker Tripped",
        "desc": "Field data circuit breaker trips in 5 minutes."
    }
},
"MongoDB": {
    "mongodb_active_reads": {
        "name": "Active Reads",
        "desc": "The number of active read operations currently being executed, used to monitor database load."
    },
    "mongodb_active_writes": {
        "name": "Active Writes",
        "desc": "The number of active write operations currently being executed, used to monitor write pressure."
    },
    "mongodb_commands": {
        "name": "Commands Per Second",
        "desc": "The number of database operations per second, reflecting database load."
    },
    "mongodb_connections_current": {
        "name": "Current Connections",
        "desc": "The number of active client connections to the database."
    },
    "mongodb_latency_commands": {
        "name": "Command Latency",
        "desc": "The average latency of database commands, used to assess database performance."
    },
    "mongodb_resident_megabytes": {
        "name": "Resident Memory Usage",
        "desc": "The amount of physical memory used by MongoDB, reflecting resource usage."
    },
    "mongodb_net_in_bytes": {
        "name": "Incoming Traffic",
        "desc": "The amount of incoming data received per second, used to monitor network traffic."
    },
    "mongodb_net_out_bytes": {
        "name": "Outgoing Traffic",
        "desc": "The amount of outgoing data sent per second, used to monitor network traffic."
    },
    "mongodb_total_docs_scanned": {
        "name": "Documents Scanned",
        "desc": "The number of documents scanned per second during queries, used to assess query performance."
    }
},
"Mysql": {
    "mysql_aborted_clients": {
        "name": "Aborted Clients",
        "desc": "This metric represents the number of connections aborted due to client errors. Monitoring this metric can help identify connection reliability issues."
    },
    "mysql_aborted_connects": {
        "name": "Aborted Connects",
        "desc": "This metric represents the number of connection attempts aborted due to connection issues. High values may indicate configuration issues or server overload."
    },
    "mysql_access_denied_errors": {
        "name": "Access Denied Errors",
        "desc": "This metric represents the number of access denials due to insufficient privileges or authentication failures. Monitoring this metric helps in identifying and resolving permission issues."
    },
    "mysql_aria_pagecache_blocks_unused": {
        "name": "Aria Pagecache Blocks Unused",
        "desc": "This metric indicates the number of unused page cache blocks in the Aria storage engine. Monitoring this metric helps optimize cache allocation."
    },
    "mysql_aria_pagecache_blocks_used": {
        "name": "Aria Pagecache Blocks Used",
        "desc": "This metric indicates the number of used page cache blocks in the Aria storage engine. Monitoring this metric helps assess the effective utilization of the cache."
    },
    "mysql_bytes_received": {
        "name": "Bytes Received",
        "desc": "This metric indicates the number of bytes received by the MySQL server. Monitoring this metric helps understand the network traffic load."
    },
    "mysql_bytes_sent": {
        "name": "Bytes Sent",
        "desc": "This metric indicates the number of bytes sent by the MySQL server. Monitoring this metric helps understand the network traffic load."
    },
    "mysql_com_select": {
        "name": "Select Commands",
        "desc": "This metric represents the number of Select queries executed. Monitoring this metric helps understand the frequency of read operations and system load."
    },
    "mysql_com_insert": {
        "name": "Insert Commands",
        "desc": "This metric represents the number of Insert commands executed. Monitoring this metric helps understand the frequency of write operations and system load."
    },
    "mysql_com_update": {
        "name": "Update Commands",
        "desc": "This metric represents the number of Update commands executed. Monitoring this metric helps understand the frequency of update operations and system load."
    },
    "mysql_com_delete": {
        "name": "Delete Commands",
        "desc": "This metric represents the number of Delete commands executed. Monitoring this metric helps understand the frequency of delete operations and system load."
    },
    "mysql_connections_total": {
        "name": "Total Connections Created",
        "desc": "This metric represents the total number of connections created since the server started. Monitoring the total connections helps understand connection patterns and load."
    }
},
"Postgres": {
    "postgresql_active_time": {
      "name": "PostgreSQL Active Time",
      "desc": "This metric indicates the total duration of the PostgreSQL instance in an active state, reflecting the duration of database activity."
    },
    "postgresql_blk_read_time": {
      "name": "PostgreSQL Block Read Time Rate",
      "desc": "Indicates the rate of time spent on block read operations by the PostgreSQL instance (in seconds per second). Used for monitoring read performance."
    },
    "postgresql_blk_write_time": {
      "name": "PostgreSQL Block Write Time Rate",
      "desc": "Indicates the rate of time spent on block write operations by the PostgreSQL instance (in seconds per second). Used for monitoring write performance."
    },
    "postgresql_blks_hit": {
      "name": "PostgreSQL Blocks Hit Rate",
      "desc": "Indicates the rate of block cache hits by the PostgreSQL instance (in hits per second). Used for monitoring cache efficiency."
    },
    "postgresql_blks_read": {
      "name": "PostgreSQL Blocks Read Rate",
      "desc": "Indicates the rate of block reads by the PostgreSQL instance (in reads per second). Used for monitoring read frequency."
    },
    "postgresql_blks_hit_ratio": {
      "name": "PostgreSQL Blocks Hit Ratio(5m)",
      "desc": "Indicates the PostgreSQL instance's block cache hit ratio over the past 5 minutes, reflecting cache effectiveness. A high hit ratio means most data requests are fulfilled from the cache, reducing disk reads and improving query performance."
    },
    "postgresql_buffers_alloc": {
      "name": "PostgreSQL Buffers Allocated Rate",
      "desc": "Indicates the rate of buffer allocations by the PostgreSQL instance (in allocations per second). Used for monitoring buffer allocation."
    },
    "postgresql_buffers_checkpoint": {
      "name": "PostgreSQL Buffers Checkpoint Rate",
      "desc": "Indicates the rate of buffers at checkpoints by the PostgreSQL instance (in checkpoints per second). Used for monitoring checkpoint frequency."
    },
    "postgresql_xact_commit": {
      "name": "PostgreSQL Transactions Committed Rate",
      "desc": "Indicates the rate of transactions committed by the PostgreSQL instance (in commits per second). Used for monitoring transaction commit frequency."
    },
    "postgresql_xact_rollback": {
      "name": "PostgreSQL Transactions Rolled Back Rate",
      "desc": "Indicates the rate of transactions rolled back by the PostgreSQL instance (in rollbacks per second). Used for monitoring transaction rollback frequency."
    },
    "postgresql_sessions": {
      "name": "PostgreSQL Active Sessions",
      "desc": "Indicates the total number of sessions for the PostgreSQL instance (including idle connections), used for monitoring connection pool usage and identifying connection leaks or abnormal surges."
    },
    "postgresql_sessions_abandoned": {
      "name": "PostgreSQL Abandoned Sessions Rate",
      "desc": "Rate of sessions abnormally disconnected due to network/client issues per second, used to identify client/network instability and resource leaks."
    },
    "postgresql_sessions_killed": {
      "name": "PostgreSQL Killed Sessions Rate",
      "desc": "Indicates the rate of killed sessions for the PostgreSQL instance (in terminations per second). Used for monitoring session termination frequency."
    }
},
"Redis": {
    "redis_used_memory": {
      "name": "Used Memory",
      "desc": "This metric indicates the memory used by the Redis allocator, including all internal data structures and caches."
    },
    "redis_mem_fragmentation_ratio": {
      "name": "Memory Fragmentation",
      "desc": "This metric indicates the memory fragmentation ratio, reflecting memory usage efficiency."
    },
    "redis_instantaneous_ops_per_sec": {
      "name": "Operations per Second",
      "desc": "This metric indicates the number of Redis commands processed per second (QPS)."
    },
    "redis_keyspace_hits": {
      "name": "Keyspace Hits",
      "desc": "This metric indicates the number of cache hits."
    },
    "redis_keyspace_misses": {
      "name": "Keyspace Misses",
      "desc": "This metric indicates the number of cache misses."
    },
    "redis_clients": {
      "name": "Connected Clients",
      "desc": "This metric indicates the current number of connected clients, reflecting active connections."
    },
    "redis_used_cpu_sys_rate": {
      "name": "Redis System CPU Rate",
      "desc": "Rate of CPU time consumed by Redis in system mode per second. High value (>1) may indicate heavy I/O operations, triggering an alert."
    },
    "redis_evicted_keys": {
      "name": "Evicted Keys",
      "desc": "This metric indicates the number of key-value pairs evicted due to memory constraints."
    },
    "redis_connected_slaves": {
      "name": "Connected Slaves",
      "desc": "This metric indicates the current number of replicas connected to the master node."
    },
    "redis_rdb_last_save_time_elapsed": {
      "name": "Last Save Elapsed Time",
      "desc": "This metric indicates the elapsed time since the last successful RDB save operation."
    },
    "redis_rejected_connections": {
      "name": "Rejected Connections",
      "desc": "This metric indicates the number of connections rejected due to server overload or policy restrictions."
    }
},
"Docker": {
    "docker_n_containers": {
        "name": "Containers Count",
        "desc": "This metric indicates the total number of containers on the Docker host, reflecting the host's load."
    },
    "docker_n_containers_running": {
        "name": "Running Containers",
        "desc": "This metric indicates the number of containers running on the Docker host, reflecting the host's load."
    },
    "docker_n_containers_stopped": {
        "name": "Stopped Containers",
        "desc": "This metric indicates the number of stopped containers on the Docker host, helping to understand container status."
    },
},
"Docker Container": {
    "docker_container_status": {
        "name": "Status",
        "desc": "This metric indicates the state of the container, where 0 means the container is normal."
    },
    "docker_container_status_restart_count": {
        "name": "Restart Count",
        "desc": "This metric indicates the number of container restarts, helping monitor if the container is frequently restarting."
    },
    "docker_container_cpu_usage_percent": {
        "name": "CPU Usage Percent",
        "desc": "This metric indicates the percentage of CPU usage of the container, monitoring the CPU load of the container."
    },
    "docker_container_mem_usage_percent": {
        "name": "Memory Usage Percent",
        "desc": "This metric indicates the percentage of memory usage of the container, monitoring the memory load of the container."
    },
    "docker_container_mem_usage": {
        "name": "Memory Usage",
        "desc": "Amount of memory used by the container, typically shown in bytes, indicating the actual physical memory consumption."
    },
    "docker_container_blkio_io_service_bytes_recursive_total": {
        "name": "Total Block I/O Bytes",
        "desc": "Total number of bytes transferred during block I/O operations in the container, including all read and write operations."
    },
    "docker_container_blkio_io_service_bytes_recursive_read": {
        "name": "Block Device Read Bytes",
        "desc": "Number of bytes read from block devices, reflecting the load of read operations and storage performance."
    },
    "docker_container_blkio_io_service_bytes_recursive_write": {
        "name": "Block Device Write Bytes",
        "desc": "Number of bytes written to block devices, indicating the load of write operations and storage performance."
    },
    "docker_container_net_rx_bytes": {
        "name": "Received Network Bytes",
        "desc": "This metric indicates the number of network bytes received by the container, used to monitor the network traffic of the container."
    },
    "docker_container_net_tx_bytes": {
        "name": "Transmitted Network Bytes",
        "desc": "This metric indicates the number of network bytes sent by the container, used to monitor the network traffic of the container."
    },
    "docker_container_net_rx_errors": {
        "name": "Total Network Receive Errors",
        "desc": "Total number of errors encountered by the container when receiving packets, useful for diagnosing network issues."
    },
    "docker_container_net_tx_errors": {
        "name": "Total Network Transmit Errors",
        "desc": "Total number of errors encountered by the container when sending packets, useful for identifying outbound network problems."
    },
    "docker_container_net_rx_packets": {
        "name": "Total Received Packets",
        "desc": "Total number of packets received by the container, indicating the activity level of inbound network flow."
    },
    "docker_container_net_tx_packets": {
        "name": "Total Transmitted Packets",
        "desc": "Total number of packets sent by the container, reflecting the activity level of outbound network flow."
    }
},
"vCenter": {
        "vmware_esxi_count": {
            "name": "Number of ESXi",
            "desc": "This metric counts the number of ESXi hosts in the VMware environment, helping administrators understand the current physical host resources."
        },
        "vmware_datastore_count": {
            "name": "Number of Datastores",
            "desc": "This metric counts the number of datastores in the VMware environment, facilitating the monitoring of storage resource allocation and usage."
        },
        "vmware_vm_count": {
            "name": "Number of VM",
            "desc": "This metric counts the number of virtual machines in the VMware environment, used to assess the utilization of virtualization resources."
        }
    },
"ESXI": {
   "esxi_cpu_usage_average_gauge": {
        "name": "CPU usage",
        "desc": "It represents the CPU utilization rate of the system or application program, measured in percent (%), which is a key indicator for measuring CPU load and performance."
    },
    "esxi_cpu_usagemhz_average_gauge": {
        "name": "CPU utilization rate",
        "desc": "It represents the CPU usage, measured in megahertz (MHz), and reflects the actual operating frequency of the CPU."
    },
    "esxi_mem_usage_average_gauge": {
        "name": "Memory utilization rate",
        "desc": "The memory utilization rate indicates the usage situation of the memory, measured in percent (%), and is used to evaluate the memory load of the system or application program."
    },
    "esxi_mem_consumed_average_gauge": {
        "name": "Active memory",
        "desc": "The active memory represents the actual amount of memory used by the system or application program, measured in megabytes (MB), and is a key indicator of memory consumption."
    },
    "esxi_disk_read_average_gauge": {
        "name": "Disk read rate",
        "desc": "The disk read rate represents the amount of data read from the disk per second, measured in megabytes per second (MB/s), and is an important indicator for measuring the disk read performance."
    },
    "esxi_disk_write_average_gauge": {
        "name": "Disk write rate",
        "desc": "The disk write rate represents the amount of data written to the disk per second, measured in megabytes per second (MB/s), and is an important indicator for measuring the disk write performance."
    },
    "esxi_disk_numberRead_summation_gauge": {
        "name": "Disk read I/O",
        "desc": "Represents the number of disk read operations completed per second, measured in IOPS (operations per second), which is an important metric for measuring the frequency of disk read requests. Higher values indicate more frequent read requests."
    },
    "esxi_disk_numberWrite_summation_gauge": {
        "name": "Disk write I/O",
        "desc": "Represents the number of disk write operations completed per second, measured in IOPS (operations per second), which is an important metric for measuring the frequency of disk write requests. Higher values indicate more frequent write requests."
    },
    "esxi_net_bytesRx_average_gauge": {
        "name": "Network receive rate",
        "desc": "The network receive rate represents the amount of data received per second, measured in kilobytes per second (KB/s), and is an important criterion for measuring network traffic."
    },
    "esxi_net_bytesTx_average_gauge": {
        "name": "Network transmit rate",
        "desc": "The network transmit rate represents the amount of data sent out per second, measured in kilobytes per second (KB/s), and is an important criterion for measuring network traffic."
    }
},
"DataStorage": {
    "data_storage_disk_used_average": {
        "name": "Disk utilization rate",
        "desc": "The disk utilization rate indicates the usage situation of disk space and is an indicator for measuring the utilization rate of disk storage."
    },
    "data_storage_disk_free_average": {
        "name": "Disk remaining capacity",
        "desc": "The remaining disk space represents the amount of unused space in the disk and is a key indicator for evaluating the disk capacity."
    },
    "data_storage_base.store_accessible": {
        "name": "Storage connection status",
        "desc": "The storage connection status indicates the connectability of the storage device and is an indicator for evaluating the health status of the storage system."
    }
},
"VM": {
     "vm_cpu_usage_average_gauge": {
        "name": "CPU utilization rate",
        "desc": "It represents the CPU utilization rate of the system within a specific time period, usually expressed as a percentage. This indicator helps to understand the CPU load situation, so as to carry out performance optimization and capacity planning."
    },
    "vm_cpu_usagemhz_average_gauge": {
        "name": "CPU usage",
        "desc": "It represents the CPU usage of the system within a specific time period, usually measured in MHz. This indicator is used to measure the actual operating frequency of the CPU and helps to analyze the consumption of CPU resources."
    },
    "vm_mem_usage_average_gauge": {
        "name": "Memory utilization rate",
        "desc": "It represents the memory utilization rate of the system within a specific time period, usually expressed as a percentage. This indicator helps to understand the memory load situation, which is helpful for optimizing memory usage and conducting capacity planning."
    },
    "vm_mem_consumed_average_gauge": {
        "name": "Active memory",
        "desc": "It represents the active memory of the system within a specific time period, usually measured in MB or GB. This indicator is used to measure the actual memory resources consumed by the system and helps to analyze the memory usage situation."
    },
    "vm_disk_io_usage_gauge": {
        "name": "Disk I/O Usage",
        "desc": "Indicates the I/O usage of the VM's disk, i.e., the busyness of the disk over a period of time. Higher values indicate higher disk load."
    },
    "vm_disk_read_average_gauge": {
        "name": "Disk Read Throughput",
        "desc": "Represents the average read throughput of the VM's disk over a period of time. Higher values indicate better read performance."
    },
    "vm_disk_used_average_gauge": {
        "name": "Disk Usage",
        "desc": "Represents the average usage of the VM's disk, i.e., the proportion of disk space used. Higher values indicate tighter disk space."
    },
    "vm_disk_numberRead_summation_gauge": {
        "name": "Disk read I/O",
        "desc": "Represents the number of disk read operations completed per second, an important metric for measuring the frequency of disk read requests. Higher values indicate more frequent read requests."
    },
    "vm_disk_numberWrite_summation_gauge": {
        "name": "Disk write I/O",
        "desc": "Represents the number of disk write operations completed per second, an important metric for measuring the frequency of disk write requests."
    },
    "vm_disk_write_average_gauge": {
        "name": "Disk Write Throughput",
        "desc": "Represents the average write throughput of the VM's disk over a period of time. Higher values indicate better write performance."
    },
    "vm_net_bytesRx_average_gauge": {
        "name": "Network receive rate",
        "desc": "It represents the network receive rate of the system within a specific time period, usually measured in MB/s or GB/s. This indicator is used to measure the network receiving performance and helps to analyze network traffic and bandwidth usage."
    },
    "vm_net_bytesTx_average_gauge": {
        "name": "Network transmit rate",
        "desc": "It represents the network transmit rate of the system within a specific time period, usually measured in MB/s or GB/s. This indicator is used to measure the network transmitting performance and helps to analyze network traffic and bandwidth usage."
    },
    "vm_power_state_gauge": {
        "name": "Power state",
        "desc": "It indicates the current power status of a virtual machine (VM). This metric helps administrators monitor whether a VM is powered on or off. This metric is essential for tracking VM availability, optimizing resource allocation, and automating workflows in VMware environments."
    }
},
    "JVM": {
    "jmx_scrape_duration_seconds_gauge": {
      "name": "JMX Scrape Duration",
      "desc": "The duration of the most recent JMX monitoring data collection, measured in seconds, is used to evaluate the performance of data collection."
    },
    "jmx_scrape_error_gauge": {
      "name": "JMX Scrape Error",
      "desc": "Indicates whether there is a failure during the JMX scraping process. A non-zero value indicates a failure"
    },
    "jvm_memory_usage_init_value": {
      "name": "JVM Memory Init",
      "desc": "The size of memory initialized and allocated when the Java Virtual Machine starts, reflecting the initial memory configuration"
    },
    "jvm_memory_usage_committed_value": {
      "name": "JVM Memory Committed",
      "desc": "The current size of memory committed for use by the Java Virtual Machine, which can be used to assess memory resource occupancy"
    },
    "jvm_memory_usage_used_value": {
      "name": "JVM Memory Used",
      "desc": "The current actual amount of memory used by the Java Virtual Machine, directly reflecting the memory usage"
    },
    "jvm_memory_usage_max_value": {
      "name": "JVM Memory Usage Max",
      "desc": "The maximum amount of memory used by the Java Virtual Machine during operation, which can be used to detect memory pressure and leaks"
    },
    "jvm_threads_total_started_count_value": {
      "name": "JVM Total Threads Started/sec",
      "desc": "The total number of threads created and started by the Java Virtual Machine since startup, showing the scale of thread creation"
    },
    "jvm_threads_daemon_count_value": {
      "name": "JVM Daemon Threads",
      "desc": "The current number of active daemon threads in the Java Virtual Machine. Daemon threads are used to serve other threads"
    },
    "jvm_threads_peak_count_value": {
      "name": "JVM Peak Threads",
      "desc": "The peak number of threads during the operation of the Java Virtual Machine, which can assist in analyzing peak thread resource usage"
    },
    "jvm_threads_count_value": {
      "name": "JVM Current Threads Count",
      "desc": "The current number of running threads in the Java Virtual Machine, real-time reflecting thread activity"
    },
    "jvm_threads_current_user_time_value": {
      "name": "JVM Thread User Time",
      "desc": "The CPU time spent by the current threads in the Java Virtual Machine executing user code, used to analyze thread performance"
    },
    "jvm_os_memory_physical_free_value": {
      "name": "Free Physical Memory",
      "desc": "The current available size of physical memory in the system, reflecting the remaining memory resources"
    },
    "jvm_os_memory_physical_total_value": {
      "name": "Total Physical Memory",
      "desc": "The total capacity of physical memory in the system, which is a fixed parameter of the hardware configuration"
    },
    "jvm_os_memory_swap_free_value": {
      "name": "Free Swap Space",
      "desc": "The current available size of swap space in the system, used to temporarily store data when physical memory is insufficient"
    },
    "jvm_os_memory_swap_total_value": {
      "name": "Total Swap Space",
      "desc": "The total capacity of swap space in the system, determining the upper limit of expandable virtual memory"
    },
    "jvm_os_memory_committed_virtual_value": {
      "name": "Committed Virtual Memory",
      "desc": "The size of virtual memory committed for use by the Java Virtual Machine, reflecting the occupancy of virtual memory resources"
    },
    "jvm_os_available_processors_value": {
      "name": "Available Processors",
      "desc": "The current number of processor cores available for executing threads in the system, affecting the program's parallel processing ability"
    },
    "jvm_os_processcputime_seconds_value": {
      "name": "JVM Process CPU Time",
      "desc": "The CPU time consumed by the Java Virtual Machine process since startup, measuring process resource occupancy"
    },
    "jvm_bufferpool_count_value": {
      "name": "BufferPool Count",
      "desc": "The number of buffer objects in the BufferPool of Java NIO, used to monitor the scale of the resource pool"
    },
    "jvm_bufferpool_memoryused_value": {
      "name": "BufferPool Memory Used",
      "desc": "The current size of memory used by the BufferPool in Java NIO, reflecting the usage of the resource pool"
    },
    "jvm_bufferpool_totalcapacity_value": {
      "name": "BufferPool Total Capacity",
      "desc": "The total memory capacity of the BufferPool in Java NIO, showing the maximum carrying capacity of the resource pool"
    },
    "jvm_gc_collectiontime_seconds_value": {
      "name": "GC Collection Time",
      "desc": "The total cumulative time consumed by garbage collection operations in the Java Virtual Machine, used to evaluate GC performance"
    },
    "jvm_gc_collectioncount_value": {
      "name": "GC Collection Count",
      "desc": "The cumulative number of garbage collection operations in the Java Virtual Machine, reflecting the frequency of GC activities"
    },
    "jvm_memorypool_usage_init_value": {
      "name": "MemoryPool Init Usage",
      "desc": "The initialized memory usage of the memory pool in the Java Virtual Machine, reflecting the initial state of the memory pool"
    },
    "jvm_memorypool_usage_committed_value": {
      "name": "MemoryPool Committed",
      "desc": "The current committed memory usage of the memory pool in the Java Virtual Machine, showing the occupancy of memory pool resources"
    },
    "jvm_memorypool_usage_used_value": {
      "name": "MemoryPool Used",
      "desc": "The current actual memory usage of the memory pool in the Java Virtual Machine, directly reflecting the usage level of the memory pool"
    },
    "jvm_memorypool_usage_max_value": {
      "name": "MemoryPool Max Usage",
      "desc": "The maximum memory usage ever reached by the memory pool during the operation of the Java Virtual Machine, which can detect memory pool pressure"
    }
  },
  "Tomcat-JMX": {
    "tomcat_bytesreceived_increase": {
      "name": "Received Bytes Increase",
      "desc": "Increase in received bytes over the past 5 minutes (in kibibytes), reflecting network input rate. A continuous increase may indicate higher network input traffic, requiring attention to network bandwidth."
    },
    "tomcat_bytessent_increase": {
      "name": "Sent Bytes Increase",
      "desc": "Increase in sent bytes over the past 5 minutes (in kibibytes), reflecting network output rate. A high value may indicate significant network output traffic, requiring attention to network bandwidth."
    },
    "tomcat_errorcount_increase": {
      "name": "Error Increase",
      "desc": "Increase in errors over the past 5 minutes, reflecting changes in error frequency. A high value may indicate numerous system issues that need prompt investigation."
    },
    "tomcat_processingtime_increase": {
      "name": "Total Processing Time Increase",
      "desc": "Increase in total time (in seconds) taken to process requests over the past 5 minutes, evaluating changes in overall processing efficiency. A continuous increase may indicate growing request processing time, suggesting further analysis for potential performance bottlenecks."
    },
    "tomcat_maxtime_total_counter": {
      "name": "Max Processing Time",
      "desc": "Maximum request processing time (in seconds) for a specific port and protocol, locating slow requests. A high value may indicate a performance bottleneck, suggesting optimization of application performance."
    },
    "tomcat_requestcount_increase": {
      "name": "Request Increase",
      "desc": "Increase in requests over the past 5 minutes, reflecting traffic trends. A continuous increase may indicate higher traffic, requiring attention to system load."
    },
    "tomcat_threadpool_currentthreadcount_gauge": {
      "name": "Current Threads",
      "desc": "Current number of threads in the thread pool, monitoring concurrent load. A high value may indicate heavy thread pool load, suggesting optimization of thread pool configuration."
    },
    "tomcat_threadpool_utilization": {
      "name": "Threadpool Utilization",
      "desc": "Utilization of the thread pool, reflecting its usage. A high value may indicate the thread pool is nearing saturation, suggesting the need to increase thread pool capacity or optimize application performance."
    },
    "tomcat_threadpool_currentthreadsbusy_gauge": {
      "name": "Busy Threads",
      "desc": "Number of busy threads, determining processing capacity bottlenecks. A high value may indicate insufficient processing capacity, suggesting optimization of thread pool configuration."
    },
    "tomcat_threadpool_running_gauge": {
      "name": "Running Threads",
      "desc": "Number of actively running threads in the thread pool, reflecting actual workload. A high value may indicate heavy thread pool load, suggesting optimization of thread pool configuration."
    },
    "tomcat_session_processingtime_avg": {
      "name": "Average Session Processing Time",
      "desc": "Over the past 5 minutes, the average session processing time per second (in milliseconds). This metric reflects the average efficiency of the system in processing sessions. A lower value indicates that the system processes sessions quickly and efficiently; a higher value may indicate performance bottlenecks in the system when processing sessions."
    },
    "tomcat_session_sessioncounter_total_counter": {
      "name": "Active Sessions",
      "desc": "Total number of active sessions for a specific host, monitoring session resource usage. A high value may indicate excessive session resource usage, suggesting optimization of session management."
    },
    "tomcat_session_expiredsessions_total_counter": {
      "name": "Expired Sessions",
      "desc": "Total number of expired sessions for a specific host, detecting session timeouts. A high value may indicate frequent session timeouts, requiring a review of session configuration or resource limits."
    },
    "tomcat_session_rejectionrate": {
      "name": "Session Rejection Rate",
      "desc": "Session rejection rate, reflecting the proportion of session creation failures. A high value may indicate issues with session management, requiring a review of session configuration or resource limits."
    },
    "jmx_scrape_error_gauge": {
      "name": "JMX Scrape Error",
      "desc": "JMX scrape status: 0 for success, 1 for failure."
    }
  },
  "Jetty-JMX": {
    "jetty_queuedthreadpool_utilizationrate_value": {
      "name": "Utilization Rate",
      "desc": "Current utilization rate of threads performing temporary jobs in the thread pool(The ratio of currently active threads to the maximum number of threads in the thread pool), indicating resource utilization pressure."
    },
    "jetty_queuedthreadpool_threads_value": {
      "name": "Thread Count",
      "desc": "Total number of threads currently managed by the thread pool, including active and idle threads."
    },
    "jetty_queuedthreadpool_maxthreads_value": {
      "name": "Maximum Threads Count",
      "desc": "The maximum number of threads allowed in the Jetty thread pool, and the time threshold after which an idle thread will be reclaimed."
    },
    "jetty_queuedthreadpool_idletimeout_value": {
      "name": "Idle Timeout for Threads",
      "desc": "Maximum allowable idle timeout for threads in Jetty thread pools."
    },
    "jetty_queuedthreadpool_readythreads_value": {
      "name": "Jetty Ready Threads",
      "desc": "The number of ready threads in the Jetty server, used to assess idle resources in the thread pool."
    },
    "jvm_memory_heap_usage_used_rate": {
      "name": "Heap Memory Usage Change Rate",
      "desc": "The average rate of change in JVM heap memory usage over 5 minutes , measured in megabytes per minute, used to monitor the trend of heap memory usage in real-time and detect memory leaks or memory pressure issues."
    },
    "jvm_memory_heap_usage_max_value": {
      "name": "Heap Memory Usage (Max)",
      "desc": "The maximum amount of heap memory available to the JVM, used to assess the upper limit of heap memory to prevent memory overflow."
    },
    "jvm_memory_heap_usage_used_value": {
      "name": "Heap Memory Usage (Used)",
      "desc": "The portion of JVM heap memory that is currently in use, used to assess the current heap memory usage."
    },
    "jvm_memory_heap_usage_committed_value": {
      "name": "Heap Memory Usage (Committed)",
      "desc": "The portion of JVM heap memory that has been committed, used to assess the actual amount of heap memory allocated to the JVM."
    },
    "jvm_memory_nonheap_usage_used_rate": {
      "name": "Non-Heap Memory Usage Change Rate",
      "desc": "The average rate of change in JVM non-heap memory usage over 5 minutes , measured in megabytes per minute, used to monitor the trend of non-heap memory usage."
    },
    "jvm_memory_nonheap_usage_max_value": {
      "name": "Non-Heap Memory Usage (Max)",
      "desc": "The maximum amount of non-heap memory available to the JVM, used to assess the upper limit of non-heap memory."
    },
    "jetty_httpconfiguration_outputbuffersize_value": {
      "name": "HTTP Output Buffer Size",
      "desc": "Represents the output buffer size (KB) for HTTP responses in Jetty, controlling data buffering to balance performance and memory usage."
    },
    "jetty_httpconfiguration_idletimeout_value": {
      "name": "HTTP Idle Timeout",
      "desc": "Indicates the maximum keep-alive time (seconds) for HTTP connections without data transfer, releasing idle resources to prevent waste and malicious occupation."
    },
    "jetty_httpconfiguration_headercachesize_value": {
      "name": "HTTP Header Cache Size",
      "desc": "Represents the maximum number of HTTP request/response headers cached by Jetty to reduce parsing overhead and improve request processing speed."
    },
    "jetty_httpconfiguration_maxerrordispatches_value": {
      "name": "Max Error Dispatches",
      "desc": "Indicates the maximum number of error dispatches allowed in Jetty to prevent infinite loops and resource exhaustion during error handling."
    },
    "jetty_bufferpool_heapmemory_value": {
      "name": "Heap Memory Reserved for Buffers",
      "desc": "Represents the heap memory usage (MB) by Jetty's buffer pool for data block caching, monitoring memory leaks and usage."
    },
    "jetty_bufferpool_heapmemory_rate": {
      "name": "Heap Memory Reserved for Buffers Rate",
      "desc": "Represents the average rate of heap memory change (MB/s) for buffers over 5 minutes, identifying usage trends and anomalies."
    },
    "jetty_arraybufferpool_directmemory_value": {
      "name": "DirectMemory Reserved for DirectBuffer",
      "desc": "Represents the direct memory usage (MB) by Jetty's direct buffers for high-performance I/O, preventing out-of-memory errors in non-heap space."
    },
    "jetty_arraybufferpool_directmemory_rate": {
      "name": "DirectMemory Reserved for DirectBuffer Rate",
      "desc": "Represents the average rate of direct memory change (MB/s) over 5 minutes, analyzing allocation patterns and leak risks."
    },
    "jetty_serverconnector_idletimeout_value": {
      "name": "Idle Timeout",
      "desc": "Indicates the idle timeout (seconds) for network connections in Jetty, managing TCP connection lifecycles to optimize long-connection resource recycling."
    },
    "jetty_managedselector_selectcount_value": {
      "name": "Selector Loop Select Count",
      "desc": "Represents the cumulative number of select() method invocations by Jetty's selector, reflecting I/O event processing frequency and network load."
    },
    "jetty_managedselector_selectcount_increase": {
      "name": "Selector Loop Select Count Increase",
      "desc": "Represents the increase in selector select() calls over 5 minutes, eliminating counter reset effects to measure I/O trends accurately."
    },
    "jetty_reservedthreadexecutor_available_value": {
      "name": "Available Reserved Threads",
      "desc": "Represents the number of available reserved threads in Jetty's executor, monitoring high-priority task pool load to avoid processing delays."
    },
    "jmx_scrape_error_gauge": {
      "name": "JMX Scrape Error",
      "desc": "JMX scrape status: 0 for success, 1 for failure."
    }
  },
  "ActiveMQ-JMX": {
    "activemq_connections_total_counter": {
      "name": "Total Connections",
      "desc": "The total number of connections to the ActiveMQ broker. Monitoring this can help detect broker load and connection management efficiency."
    },
    "activemq_connections_total_rate": {
      "name": "Connections Rate",
      "desc": "Connection rate over 5 minutes, used to monitor connection establishment frequency."
    },
    "activemq_connections_gauge": {
      "name": "Current Connections",
      "desc": "The number of active connections to the ActiveMQ broker. This helps to understand real-time connection status and potential bottlenecks."
    },
    "activemq_topic_memory_percent_usage_value": {
      "name": "Memory Percent Usage",
      "desc": "Shows the percentage of memory consumption, which helps in optimizing resource allocation to prevent performance degradation."
    },
    "activemq_topic_memory_usage_byte_count_value": {
      "name": "Memory Usage Byte Count",
      "desc": "The memory occupied by undelivered messages, which helps assess the broker's memory consumption and management strategy."
    },
    "activemq_memory_usage_ratio_gauge": {
      "name": "Memory Usage Ratio",
      "desc": "The percentage of memory usage limits in the system, helpful for managing and optimizing memory use."
    },
    "activemq_topic_queue_size_value": {
      "name": "Queue Size",
      "desc": "The total amount of messages yet to be consumed, indicating the broker's workload and processing capacity."
    },
    "activemq_topic_enqueue_count_value": {
      "name": "Enqueue Count",
      "desc": "Number of messages received by the target, essential for monitoring communication traffic and flow control measures."
    },
    "activemq_topic_enqueue_rate": {
      "name": "Enqueue Rate",
      "desc": "The number of messages enqueued per unit of time, used for real-time monitoring of system load and message processing capabilities."
    },
    "activemq_dequeue_total_counter": {
      "name": "Total Dequeues",
      "desc": "Total number of messages confirmed and processed in the broker, which helps understand overall performance and efficiency."
    },
    "activemq_message_total_counter": {
      "name": "Unacknowledged Messages",
      "desc": "Total number of unacknowledged messages in the system, helping to identify potential message backlog issues."
    },
    "activemq_message_total_rate": {
      "name": "Unacknowledged Message Growth Rate",
      "desc": "The growth rate of unacknowledged messages over 5 minutes, used to monitor message backlog. If the growth rate remains high, it may indicate processing bottlenecks or message backlog issues in the system."
    },
    "activemq_enqueue_total_counter": {
      "name": "Total Enqueues",
      "desc": "Total number of messages sent to the broker, reflecting the system's load and communication frequency."
    },
    "activemq_topic_expired_count_value": {
      "name": "Expired Messages Count",
      "desc": "Shows the number of expired messages, indicating potential message processing delays or insufficient consumer processing capabilities."
    },
    "activemq_topic_blocked_sends_value": {
      "name": "Blocked Sends Count",
      "desc": "Shows the number of messages blocked due to flow control, helping to assess the system's flow control state and message sending smoothness."
    },
    "activemq_producer_total_counter": {
      "name": "Total Producers",
      "desc": "Shows the total number of producers currently connected to the ActiveMQ broker, helping to understand producer load and message sending activity."
    },
    "activemq_topic_producer_flow_control_value": {
      "name": "Producer Flow Control Status",
      "desc": "Indicates whether flow control is enabled for producers on the specified topic, with 1 for enabled and 0 for disabled, to prevent producers from overwhelming the system with too many messages."
    },
    "activemq_consumer_total_counter": {
      "name": "Total Consumers",
      "desc": "Shows the total number of consumers currently connected to the ActiveMQ broker, helping to understand consumer load and message processing capability."
    },
    "activemq_store_usage_ratio_gauge": {
      "name": "Store Usage Ratio",
      "desc": "The percentage of persistent store usage, helping to optimize storage management and resource allocation."
    },
    "jvm_memory_heap_usage_max_value": {
      "name": "Heap Memory Usage (Max)",
      "desc": "The maximum amount of heap memory available to the JVM, used to assess the upper limit of heap memory to prevent memory overflow."
    },
    "jvm_memory_heap_usage_used_value": {
      "name": "Heap Memory Usage (Used)",
      "desc": "The portion of JVM heap memory that is currently in use, used to assess the current heap memory usage."
    },
    "jvm_memory_nonheap_usage_used_rate": {
      "name": "Non-Heap Memory Usage Change Rate",
      "desc": "The average rate of change in JVM non-heap memory usage over 5 minutes , measured in megabytes per minute, used to monitor the trend of non-heap memory usage."
    },
    "jmx_scrape_error_gauge": {
      "name": "JMX Scrape Error",
      "desc": "JMX scrape status: 0 for success, 1 for failure."
    }
  },
  "WebLogic-JMX": {
    "weblogic_threadpool_throughput_value": {
      "name": "Thread Pool Throughput",
      "desc": "The number of requests processed per second by the thread pool, reflecting processing capacity. A higher value indicates stronger request processing capability. A significant drop in throughput may indicate performance bottlenecks or insufficient resources in the thread pool."
    },
    "weblogic_threadpool_pending_user_request_count_value": {
      "name": "Pending User Requests",
      "desc": "The length of the user request queue waiting to be processed by the thread pool. Continuous growth may lead to response delays. If this metric keeps increasing, it indicates that the thread pool cannot process requests as fast as they arrive, which may degrade user experience."
    },
    "weblogic_threadpool_queue_length_value": {
      "name": "Thread Pool Queue Length",
      "desc": "The number of tasks in the thread pool request queue, reflecting request backlog. A long queue length means many requests are waiting to be processed, which may require increasing thread pool resources or optimizing request processing logic."
    },
    "weblogic_threadpool_stuck_thread_count_value": {
      "name": "Stuck Thread Count",
      "desc": "The number of threads that have been running for a long time without completing, possibly indicating deadlocks or slow queries. When this metric is greater than 0, it is necessary to investigate whether there are code logic issues or database query performance problems."
    },
    "weblogic_threadpool_load_ratio": {
      "name": "Thread Pool Load Ratio",
      "desc": "Evaluate the load pressure of the thread pool. A value greater than 1 indicates that the request exceeds the processing capacity, and a value of 80% should trigger a severe warning. This metric helps determine whether the thread pool is overloaded, so that measures can be taken in time to prevent system crashes."
    },
    "weblogic_threadpool_average_utilization": {
      "name": "Thread Pool Average Utilization",
      "desc": "Reflect the average utilization rate of the thread pool over a period of time. High utilization may lead to thread pool overload, while low utilization may indicate resource waste. It is generally recommended to maintain it between 60% and 80%."
    },
    "weblogic_application_healthstatejmx_is_critical_value": {
      "name": "Application Health Critical State",
      "desc": "Flag indicating whether the application is in a critical abnormal state, directly reflecting business availability. When this metric is 1, it indicates that the application has a serious problem that needs to be investigated and repaired immediately."
    },
    "weblogic_application_overallhealthstatejmx_is_critical_value": {
      "name": "Application Overall Health Critical State",
      "desc": "Flag indicating whether the overall health state of the application, evaluated based on multiple metrics, is critically abnormal. When this metric is 1, it indicates that the overall health of the application is poor, which may affect the normal operation of the business."
    },
    "weblogic_workmanager_stuck_thread_count_value": {
      "name": "Global WorkManager Stuck Threads",
      "desc": "The number of stuck threads in the global work manager, used for system-level thread issue troubleshooting. When this metric is greater than 0, it is necessary to check whether there are thread blocking or resource contention issues in the system."
    },
    "weblogic_workmanager_pending_requests_value": {
      "name": "Global WorkManager Pending Requests",
      "desc": "The number of requests waiting to be processed in the global work manager. If this metric keeps increasing, it may affect the system's response speed."
    },
    "weblogic_jms_jmsservers_current_count_value": {
      "name": "JMS Servers Current Count",
      "desc": "The current number of running JMS server instances. Changes in the number may affect the performance and reliability of message delivery."
    },
    "weblogic_jms_connections_high_count_value": {
      "name": "JMS Connections High Watermark",
      "desc": "The historical highest record of JMS connections, used to evaluate the rationality of connection pool configuration. If the current number of connections is close to the peak value, it may be necessary to adjust the size of the connection pool."
    },
    "weblogic_jms_connections_current_count_value": {
      "name": "JMS Current Connections",
      "desc": "The current number of established JMS connections. Too many connections may lead to resource tension, while too few may affect the efficiency of message delivery."
    },
    "weblogic_persistentstore_object_count_value": {
      "name": "Persistent Store Object Count",
      "desc": "The current number of objects (such as messages, transaction logs) stored in the persistent store. Too many objects may lead to insufficient storage space, which requires regular cleanup."
    },
    "weblogic_persistentstore_physical_write_count_value": {
      "name": "Persistent Store Physical Rate",
      "desc": "Indicates the number of physical writes per second in the persistent store, reflecting write load. A high write frequency may lead to a decline in storage performance."
    },
    "weblogic_persistentstore_read_count_value": {
      "name": "Persistent Store Reads",
      "desc": "The number of read operations performed by the persistent store, reflecting read load. Frequent read operations may affect storage performance, and it is necessary to optimize read strategies."
    },
    "weblogic_persistentstore_total_io_rate_value": {
      "name": "Persistent Store Total I/O Rate",
      "desc": "Indicates the total number of I/O operations per second in the persistent store, including reads and writes. A high I/O frequency may lead to storage performance bottlenecks, and it is necessary to pay attention to the performance metrics of the storage system."
    },
    "jmx_scrape_error_gauge": {
      "name": "JMX Scrape Error",
      "desc": "JMX scrape status: 0 for success, 1 for failure."
    }
  },
  "TCP": {
  },
  "CVM": {
    "cvm_CPU_Usage": {
        "name": "CPU Utilization",
        "desc": "The real-time percentage of CPU occupied during machine operation."
    },
    "cvm_MemUsed": {
        "name": "Memory Usage",
        "desc": "The actual memory used by the user, excluding memory occupied by buffers and system cache. Calculated as Total Memory - Available Memory (including buffers and cached), which does not include buffers and cached."
    },
    "cvm_MemUsage": {
        "name": "Memory Utilization",
        "desc": "The actual memory utilization rate by the user, excluding memory occupied by buffers and system cache. It is the ratio of actual user memory usage to total memory, excluding cache, buffers, and free memory."
    },
    "cvm_CvmDiskUsage": {
        "name": "Disk Utilization",
        "desc": "The percentage of used disk capacity relative to total capacity (all disks)."
    },
    "cvm_LanOuttraffic": {
        "name": "Internal Outbound Bandwidth",
        "desc": "Average outbound traffic per second on the internal network interface card."
    },
    "cvm_LanIntraffic": {
        "name": "Internal Inbound Bandwidth",
        "desc": "Average inbound traffic per second on the internal network interface card."
    },
    "cvm_LanOutpkg": {
        "name": "Internal Outbound Packet Rate",
        "desc": "Average outbound packet rate per second on the internal network interface card."
    },
    "cvm_LanInpkg": {
        "name": "Internal Inbound Packet Rate",
        "desc": "Average inbound packet rate per second on the internal network interface card."
    },
    "cvm_WanOuttraffic": {
        "name": "External Outbound Bandwidth",
        "desc": "Average outbound traffic rate per second on the external network. The minimum granularity data is calculated as total traffic over 10 seconds divided by 10. This data represents the sum of outbound/inbound bandwidth from EIP+CLB+CVM on the external network."
    },
    "cvm_WanIntraffic": {
        "name": "External Inbound Bandwidth",
        "desc": "Average inbound traffic rate per second on the external network. The minimum granularity data is calculated as total traffic over 10 seconds divided by 10. This data represents the sum of outbound/inbound bandwidth from EIP+CLB+CVM on the external network."
    },
    "cvm_WanOutpkg": {
        "name": "External Outbound Packet Rate",
        "desc": "Average outbound packet rate per second on the external network interface card."
    },
    "cvm_WanInpkg": {
        "name": "External Inbound Packet Rate",
        "desc": "Average inbound packet rate per second on the external network interface card."
    }
  },
  "Oracle-Exporter": {
    "oracledb_up_gauge": {
      "name": "OracleDb Status",
      "desc": "The current Oracle database is running in the current state, 0 is normal, and 1 is abnormal."
    },
    "oracledb_uptime_seconds_gauge": {
      "name": "OracleDb Instance Uptime",
      "desc": "The duration for which the Oracle database has been running."
    },
    "oracledb_activity_execute_rate": {
      "name": "OracleDb Execution Rate",
      "desc": "Monitors the rate of SQL executions over a period (e.g., 5m) to reflect load changes."
    },
    "oracledb_activity_parse_rate": {
      "name": "OracleDb Parse Count Rate",
      "desc": "Monitors the rate of SQL parses in a period (e.g., 5m) to help identify frequent parsing issues."
    },
    "oracledb_activity_user_commits_rate": {
      "name": "OracleDb User Commits Rate",
      "desc": "Monitors the rate of user transaction commits over a period (e.g., 5m) to reflect transactional activity."
    },
    "oracledb_activity_user_rollbacks_rate": {
      "name": "OracleDb User Rollbacks Rate",
      "desc": "Monitors the rate of user transaction rollbacks over a period (e.g., 5m) to identify unusual transactions."
    },
    "oracledb_wait_time_application_gauge": {
      "name": "OracleDb Application Wait Time",
      "desc": "The waiting time for communication between the database client application and the database."
    },
    "oracledb_wait_time_commit_gauge": {
      "name": "OracleDb Commit Wait Time",
      "desc": "The time waiting for transaction commit completion."
    },
    "oracledb_wait_time_concurrency_gauge": {
      "name": "OracleDb Concurrency Wait Time",
      "desc": "The waiting time caused by database resource contention, such as waiting for locks."
    },
    "oracledb_wait_time_configuration_gauge": {
      "name": "OracleDb Configuration Wait Time",
      "desc": "The time waiting for system resource configuration, such as waiting for parameter changes to take effect."
    },
    "oracledb_wait_time_network_gauge": {
      "name": "OracleDb Network Wait Time",
      "desc": "The time waiting for network transmission, such as waiting for data to be sent from the client to the server."
    },
    "oracledb_wait_time_other_gauge": {
      "name": "OracleDb Other Wait Time",
      "desc": "The waiting time that cannot be classified into other waiting times."
    },
    "oracledb_wait_time_system_io_gauge": {
      "name": "OracleDb System I/O Wait Time",
      "desc": "The time waiting for the system to perform I/O operations, such as waiting for data to be read from the disk."
    },
    "oracledb_wait_time_user_io_gauge": {
      "name": "OracleDb User I/O Wait Time",
      "desc": "The time waiting for the user I/O operation to complete."
    },
    "oracledb_resource_utilization_rate": {
      "name": "OracleDb Resource Utilization rate",
      "desc": "The utilization rate of a resource in the current Oracle DB instance, which reflects the percentage of resources such as sessions, processes, memory, and so on that resource limits are used. If the value is negative（-）, the resource is not restricted, that is, the resource can be used indefinitely. In this case, it doesn't make much sense to monitor metrics for that dimension."
    },
    "oracledb_process_count_gauge": {
      "name": "OracleDb Processes",
      "desc": "The number of currently active database processes."
    },
    "oracledb_sessions_value_gauge": {
      "name": "OracleDb Sessions",
      "desc": "The current number of open sessions in the database. Dimension meaning: Status: Session status, such as ACTION, INACTIVE, BLOCKED, KILLED, etc. Type: Session type, such as Backend, CDB, PDB, SYS, USER, etc."
    },
    "oracledb_sga_total_gauge": {
      "name": "OracleDb SGA Total Size",
      "desc": "SGA is a shared memory area allocated in memory by an Oracle database instance to store global data and information to support the operation and access of the database instance. This metric is used to represent the total memory size of SGA and is used to measure the overall resource allocation scale of SGA."
    },
    "oracledb_sga_free_gauge": {
      "name": "OracleDb SGA Free Size",
      "desc": "Represents the amount of memory currently available for the Oracle Database SGA, reflecting the amount of unused idle resources in the SGA."
    },
    "oracledb_sga_used_percent_gauge": {
      "name": "OracleDb SGA Usage Percentage",
      "desc": "Represents the memory usage of the Oracle Database SGA and is used to evaluate the efficiency of the SGA's resources."
    },
    "oracledb_pga_total_gauge": {
      "name": "OracleDb PGA Total Size",
      "desc": "A PGA is an independently allocated area of memory for each user process or server process in an Oracle database instance that stores data and information for sessions or operations. This metric is used to represent the total memory size of the PGA and reflect the overall resource allocation scale of the PGA."
    },
    "oracledb_pga_used_gauge": {
      "name": "OracleDb PGA Used Size",
      "desc": "Represents the amount of memory currently used by the Oracle Database PGA, reflecting the actual consumption of PGA resources."
    },
    "oracledb_pga_used_percent_gauge": {
      "name": "OracleDb PGA Usage Percentage",
      "desc": "Represents the memory usage of the Oracle Database PGA, which is a measure of how efficiently the PGA resources are being utilized."
    },
    "oracledb_tablespace_bytes_gauge": {
      "name": "OracleDb Table Used Space",
      "desc": "The total size of the used disk space in the specified tablespace."
    },
    "oracledb_tablespace_max_bytes_gauge": {
      "name": "OracleDb Table Maximum Capacity",
      "desc": "The maximum disk space limit of the specified tablespace."
    },
    "oracledb_tablespace_free_gauge": {
      "name": "OracleDb Table Available Space",
      "desc": "The size of the remaining disk space in the specified tablespace."
    },
    "oracledb_tablespace_used_percent_gauge": {
      "name": "OracleDb Tablespace Usage Percentage",
      "desc": "The percentage of the used capacity of the specified tablespace."
    },
    "oracledb_rac_node_gauge": {
      "name": "OracleDb RAC Node Count",
      "desc": "The current number of Oracle database cluster nodes."
    },
    "process_cpu_seconds_total_counter": {
      "name": "OracleDb Monitoring Probe Process CPU Time",
      "desc": "The total amount of CPU time used by the Oracle Database Monitoring Probe process."
    },
    "process_max_fds_gauge": {
      "name": "OracleDb Monitoring Probe Process Max File Descriptors",
      "desc": "The maximum number of file descriptors that can be opened by the Oracle Database Monitoring Probe process."
    },
    "process_open_fds_gauge": {
      "name": "OracleDb Monitoring Probe Process Open File Descriptors",
      "desc": "The number of file descriptors that are currently open by the Oracle Database Monitoring Probe process."
    },
    "process_resident_memory_bytes_gauge": {
      "name": "OracleDb Monitoring Probe Process Resident Memory",
      "desc": "The size of the current resident memory of the Oracle Database monitoring probe process."
    },
    "process_virtual_memory_bytes_gauge": {
      "name": "OracleDb Monitoring Probe Process Virtual Memory",
      "desc": "The current virtual memory size of the Oracle Database Monitoring Probe process."
    },
    "oracledb_exporter_last_scrape_duration_seconds_gauge": {
      "name": "OracleDb Exporter Last Scrape Duration",
      "desc": "The time spent on the most recent collection of indicators from the Oracle database."
    },
    "oracledb_exporter_last_scrape_error_gauge": {
      "name": "OracleDb Exporter Last Scrape Status",
      "desc": "Whether an error occurred when the OracleDB monitoring probe collected indicators in the most recent time."
    },
    "oracledb_exporter_scrapes_total_counter": {
      "name": "OracleDb Exporter Scrape Metrics Total",
      "desc": "The total number of times of collecting indicators since the OracleDB monitoring probe was started, and if the process is restarted, it will be recalculated."
    }
  },
  "Minio": {
    "minio_audit_failed_messages_counter": {
      "name": "Unsent Msgs Total",
      "desc": "Counts unsent messages to detect sending failures and ensure message delivery integrity."
    },
    "minio_audit_target_queue_length_gauge": {
      "name": "Unsent Msgs in Target Queue",
      "desc": "Reflects message backlog in target queue for optimizing message processing."
    },
    "minio_audit_total_messages_counter": {
      "name": "Total Sent Msgs",
      "desc": "Evaluates sending success rate with unsent messages to measure stability."
    },
    "minio_audit_delivery_success_rate": {
      "name": "Message delivery success rate",
      "desc": "The success rate of sending messages is used to measure the reliability and stability of audit message sending."
    },
    "minio_cluster_capacity_usable_free_bytes_gauge": {
      "name": "Cluster Usable Free Cap",
      "desc": "Reflects available storage for data storage planning."
    },
    "minio_cluster_capacity_usable_total_bytes_gauge": {
      "name": "Cluster Used Cap",
      "desc": "Counts used storage for calculating utilization rate."
    },
    "minio_cluster_capacity_storage_utilization": {
      "name": "Cluster storage capacity utilization",
      "desc": "Collect statistics on the percentage of used capacity in the cluster storage capacity to the total capacity, monitor the storage resource usage, and evaluate the remaining storage resources."
    },
    "minio_cluster_drive_offline_total_gauge": {
      "name": "Total Offline Drives",
      "desc": "Counts offline drives to troubleshoot issues affecting performance and data availability."
    },
    "minio_cluster_drive_online_total_gauge": {
      "name": "Total Online Drives",
      "desc": "Evaluates available storage devices to ensure cluster operation."
    },
    "minio_cluster_drive_total_gauge": {
      "name": "Total Drives in Cluster",
      "desc": "Evaluates overall storage device status with online and offline counts."
    },
    "minio_cluster_drive_offline_rate": {
      "name": "Cluster drive offline rate",
      "desc": "The ratio of the number of offline drives to the total number of drives, a measure of the reliability and availability of storage devices, can affect data redundancy when thresholds such as 5% are exceeded."
    },
    "minio_cluster_nodes_offline_total_gauge": {
      "name": "Total Offline Nodes",
      "desc": "Counts offline nodes to address issues affecting performance and redundancy."
    },
    "minio_cluster_nodes_online_total_gauge": {
      "name": "Total Online Nodes",
      "desc": "Evaluates available cluster resources to ensure service capacity."
    },
    "minio_cluster_nodes_offline_rate": {
      "name": "Cluster nodes offline rate",
      "desc": "The percentage of the number of offline nodes in the total number of nodes reflects the health status of the cluster nodes and is used to evaluate the stability of the cluster nodes."
    },
    "minio_cluster_write_quorum_gauge": {
      "name": "Cluster Max Write Acks",
      "desc": "Ensures data write consistency and reliability, affecting write performance."
    },
    "minio_cluster_health_status_gauge": {
      "name": "Cluster Health Status",
      "desc": "Reflects overall cluster health for quick status check. 0 = Unhealthy, 1 = Healthy"
    },
    "minio_s3_traffic_sent_bytes_rate": {
      "name": "S3 Traffic Sent Rate",
      "desc": "Calculates the average rate of data sent in S3 requests over the past 5 minutes, reflecting data upload performance."
    },
    "minio_s3_traffic_received_bytes_rate": {
      "name": "S3 Traffic Received Rate",
      "desc": "Calculates the average rate of data received in S3 requests over the past 5 minutes, reflecting data download performance."
    },
    "minio_s3_requests_waiting_total_gauge": {
      "name": "Total Waiting S3 Requests",
      "desc": "Displays the number of S3 requests waiting to be processed, optimizes request processing efficiency, and directly reflects whether the system is saturated."
    },
    "minio_s3_requests_total_rate": {
      "name": "S3 Requests Rate",
      "desc": "Calculates the average processing rate of S3 requests over the last 5 minutes, reflecting system throughput and service load and performance baselines."
    },
    "minio_s3_requests_errors_total_rate": {
      "name": "S3 Requests Error Rate",
      "desc": "Calculates the average rate of errors in S3 requests over the past 5 minutes, reflecting system stability."
    },
    "minio_s3_requests_rejected_invalid_total_rate": {
      "name": "S3 Invalid Requests Rate",
      "desc": "Calculates the average rate of S3 requests rejected due to invalid format or parameters over the past 5 minutes, reflecting client request quality."
    },
    "minio_s3_requests_rejected_auth_total_rate": {
      "name": "S3 Auth Failure Rate",
      "desc": "Calculates the average rate of S3 requests rejected due to authentication failures over the past 5 minutes, reflecting authentication issues."
    },
    "minio_bucket_usage_object_total_gauge": {
      "name": "Total Objects in Bucket",
      "desc": "Statistics on the number of objects in a specified bucket are used to understand the data scale of the bucket and evaluate the bucket usage."
    },
    "minio_bucket_usage_total_bytes_gauge": {
      "name": "Total Bucket Size",
      "desc": "Statistics on the amount of storage space occupied by a specified bucket can be used to monitor storage resource consumption and plan storage capacity."
    },
    "minio_bucket_requests_4xx_errors_total_rate": {
      "name": "Total Bucket S3 Request Error Rate (4xx)",
      "desc": "The rate per second of client errors (e.g., 403/404) in S3 requests received by the bucket over the past 5 minutes, reflecting the real-time frequency of client request legitimacy issues."
    },
    "minio_bucket_requests_inflight_total_gauge": {
      "name": "Bucket Total Running S3 Requests",
      "desc": "Statistics on the number of S3 requests processed by a specified bucket can be used to monitor the request processing progress and optimize system performance."
    },
    "minio_bucket_requests_total_rate": {
      "name": "Bucket S3 Total Requests Rate",
      "desc": "The growth rate per second of the total number of S3 requests received by a bucket reflects the intensity of request traffic and the frequency of business access to the bucket."
    },
    "minio_bucket_traffic_received_rate": {
      "name": "Bucket Traffic Receive Rate",
      "desc": "The average amount of data traffic received by the compute bucket per second over a 5-minute period, converted to MB/s units, is used to monitor bandwidth usage for data downloads or reads."
    },
    "minio_node_drive_total_inodes_gauge": {
      "name": "Total Inodes of Drive",
      "desc": "Counts the total number of inodes on a specified drive to measure its file-storage capacity limit and evaluate the scale of storage resources."
    },
    "minio_node_drive_used_inodes_utilization": {
      "name": "Drive inode utilization",
      "desc": "Statistics on the percentage of inodes used by a specified drive can be used to understand the degree of drive usage and assist in storage resource management."
    },
    "minio_node_drive_reads_per_sec_gauge": {
      "name": "Drive Reads per Second",
      "desc": "Counts the number of read operations per second on a specified drive to evaluate its read performance and troubleshoot read-related performance issues."
    },
    "minio_node_drive_reads_kb_per_sec_gauge": {
      "name": "Drive Read Kilobytes per Second",
      "desc": "Counts the amount of data read per second (in kilobytes) on a specified drive, directly reflecting its read bandwidth to optimize data-reading strategies."
    },
    "minio_node_drive_writes_per_sec_gauge": {
      "name": "Drive Writes per Second",
      "desc": "Counts the number of write operations per second on a specified drive to evaluate its write performance and analyze the impact of write operations on the system."
    },
    "minio_node_drive_writes_kb_per_sec_gauge": {
      "name": "Drive Write Kilobytes per Second",
      "desc": "Counts the amount of data written per second (in kilobytes) on a specified drive, reflecting its write bandwidth to improve data-writing efficiency."
    },
    "minio_node_drive_perc_util_gauge": {
      "name": "Drive Busy Time Utilization",
      "desc": "Counts the percentage of time a specified drive is busy to evaluate its load and allocate storage tasks reasonably."
    },
    "minio_node_if_rx_bytes_rate": {
      "name": "The amount of data received per second",
      "desc": "Statistics on the amount of data received per second by a specified server network interface in the past five minutes are used to monitor network traffic inflow and evaluate network bandwidth usage."
    },
    "minio_node_if_rx_errors_rate": {
      "name": "Receive error rate (per second)",
      "desc": "Statistics on the number of errors that occur when receiving data per second on a specified server network interface in the past 5 minutes is used to troubleshoot network receiving faults and ensure network data transmission quality."
    },
    "minio_node_if_tx_bytes_rate": {
      "name": "The amount of data transferred per second",
      "desc": "Statistics on the amount of data transmitted per second on a specified server network interface in the past five minutes are used to monitor network traffic outflow and evaluate network bandwidth efficiency."
    },
    "minio_node_if_tx_errors_rate": {
      "name": "Transmission error rate (per second)",
      "desc": "Statistics on the number of errors that occur during data transmission per second on the network interface of a specified server in the past 5 minutes are used to troubleshoot network transmission faults and improve network communication reliability."
    },
    "minio_node_cpu_avg_load1_gauge": {
      "name": "CPU 1-Minute Average Load",
      "desc": "Calculate the average load of the CPU in the past 1 minute, reflecting the number of processes waiting for CPU resources (including running and waiting processes), the larger the value, the more CPU tension, for real-time monitoring of real-time pressure and detection of performance problems."
    },
    "minio_node_cpu_avg_load5_gauge": {
      "name": "CPU 5-Minute Average Load",
      "desc": "Calculate the average CPU load over the past 5 minutes, reflecting the number of processes waiting for CPU resources (including running and waiting processes), which is used to evaluate short-term load trends and assist in performance optimization decisions."
    },
    "minio_node_cpu_avg_load15_gauge": {
      "name": "CPU 15-Minute Average Load",
      "desc": "The average CPU load in the past 15 minutes is calculated, reflecting the number of processes waiting for CPU resources (including running and waiting processes), which is used to analyze the long-term load and plan system resources."
    }
  }
}

LANGUAGE_DICT = {
    "MONITOR_OBJECT_TYPE": MONITOR_OBJECT_TYPE,
    "MONITOR_OBJECT": MONITOR_OBJECT,
    "MONITOR_OBJECT_PLUGIN": MONITOR_OBJECT_PLUGIN,
    "MONITOR_OBJECT_METRIC_GROUP": MONITOR_OBJECT_METRIC_GROUP,
    "MONITOR_OBJECT_METRIC": MONITOR_OBJECT_METRIC,
}

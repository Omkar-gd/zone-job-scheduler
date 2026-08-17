# Cloud, Security & IoT Deployment Blueprint
## Task 9 — Distributed Architecture and Communication Plan

## Chosen Architecture: Client-Server
The platform uses a Client-Server architecture.
The three zone controllers (Zone-A, Zone-B and Zone-C) act as clients,
while the central Smart City Operations Dashboard and cloud services act
as the server-side platform.
The scheduler and Banker's-Algorithm engine from Part 1 runs as the
Cloud Platform Layer that processes the sensor-processing jobs and performs
deadlock-safety checks.

## Why Client-Server?
1. Centralized management:
   The central platform can coordinate the three zone controllers and
   provide a single view of the city's sensor-processing system.

2. Scalability:
   Additional zone controllers can be connected to the central platform
   without changing the basic architecture.

3. Security:
   Authentication, authorization, TLS and network security controls can
   be centrally managed between zone controllers and the cloud platform.

4. Fault management:
   The central platform can monitor zone controllers and detect failures
   or unavailable controllers.

## Data Flow A — Real-Time Public-Safety Alert
A zone controller publishes a real-time public-safety alert to the
Smart City Operations Dashboard.
Communication type: Synchronous.
Protocol: HTTPS over TCP.
Reason:
The alert is time-sensitive and the zone controller should receive a
reliable response confirming that the dashboard received the alert.
HTTPS also provides encrypted communication.

## Data Flow B — Daily Sensor Log Archival
A zone controller uploads its full day's sensor log to cloud storage
for archival.
Communication type: Asynchronous.
Protocol: MQTT over TCP.
Reason:
The daily log does not require an immediate response from the dashboard.
An asynchronous message-based approach allows the zone controller to
upload data without waiting for the archival service to finish processing
the complete log. MQTT is lightweight and suitable for IoT communication.

## Part 1 Engine
The scheduler and Banker's-Algorithm engine implemented in Part 1 is
the fixed compute engine used by this deployment. It runs as part of the
Cloud Platform Layer and processes the zone-controller jobs while also
performing deadlock-safety checks.



## Task 10 — VPC-Based Network Boundary
## VPC Design
The deployment uses one VPC containing three separate private subnets:
- Zone-A subnet — contains Zone-A resources
- Zone-B subnet — contains Zone-B resources
- Zone-C subnet — contains Zone-C resources
The three zones are logically isolated using separate subnets and
network-level access-control rules.
A single VPC is preferred because it provides centralized networking
while still allowing each zone to have its own subnet-level security
rules and routing controls. This provides logical isolation and
customizability without the complexity of managing multiple VPCs.
The scheduler and Banker's-Algorithm engine from Part 1 runs in the
protected Cloud Platform Layer and communicates with the zone resources
only through explicitly permitted network paths.

## Cross-Zone Protection
Zone-A and Zone-B are not allowed to communicate directly.
The specific network-level control enforcing this boundary is a
firewall/security-group rule.
The security rule denies inbound traffic from the Zone-B subnet's
network range to the Zone-A subnet/resources.
For example:
- Source: Zone-B subnet
- Destination: Zone-A subnet
- Action: DENY
Only explicitly permitted application traffic to the appropriate
cloud services is allowed.
The Smart City Operations Dashboard is not used as the security
boundary. The firewall/security-group rule itself enforces the
cross-zone isolation.



## Task 11 — Network-Security Objectives and Controls
The following six network-security objectives protect the platform and
the scheduler and Banker's-Algorithm engine from Part 1.

## 1. Protect Sensitive Data
Control: Encryption at Rest
Sensitive data such as the JOBS list, sensor logs and stored public-safety
records are encrypted when stored. This prevents unauthorized users from
reading stored data even if the storage system is accessed.

## 2. Authentication
Control: Multi-Factor Authentication (MFA)
MFA requires users and administrators to provide more than one form of
verification before accessing the cloud platform. This reduces the risk
of unauthorized account access.

## 3. Authorization
Control: Role-Based Access Control (RBAC)
RBAC gives users only the permissions required for their role. For
example, a zone operator can access zone data while an administrator
can manage security settings.

## 4. Prevent Cyber Attacks
Control: Web Application Firewall (WAF)
A WAF filters malicious HTTP/HTTPS requests before they reach the
application. It helps protect the Smart City platform from common
web-based attacks.

## 5. Secure Communication
Control: TLS 1.3
TLS 1.3 encrypts communication between zone controllers and cloud
services. It protects sensor data and public-safety alerts while they
are travelling across the network.

## 6. Ensure Availability
Control: Load Balancer
A load balancer distributes incoming requests across available service
instances. If one instance becomes unavailable, traffic can be directed
to another healthy instance, helping keep the platform available.

## Part 1 Engine
The scheduler and Banker's-Algorithm engine from Part 1 is protected by
these network-security controls when it runs in the Cloud Platform Layer.
Only authenticated and authorized communication is allowed to reach the
engine and its supporting services.



## Task 12 — IAM Table and Data-Protection Map
## IAM Roles
The platform uses Role-Based Access Control and the principle of least
privilege. Each role receives only the permissions required to perform
its job.
| IAM Role | Permissions |
|---|---|
| Zone Operator | Read sensor data, submit zone jobs, view zone status |
| City Dashboard Admin | Read data from all zones, manage dashboard settings, view alerts |
| Security Auditor | Read security logs, audit access records, view configuration; no permission to modify data |
The scheduler and Banker's-Algorithm engine from Part 1 runs as the
protected Cloud Platform Layer and uses only the permissions required
for scheduling jobs and performing safety checks.

## Data Protection Map
## 1. Data at Rest
Protection: Encryption at Rest
Example:
The JOBS list and stored sensor logs on the zone controller or cloud
storage are encrypted while stored.

## 2. Data in Transit
Protection: TLS 1.3
Example:
A public-safety alert travelling from a zone controller to the Smart
City Operations Dashboard is protected using TLS 1.3.

## 3. Data in Use
Protection: Access Control and Memory Protection
Example:
The Banker's-Algorithm safety check from Part 1 processes allocation,
need and available-resource information in memory. Only the authorized
scheduler process can access this information.

## Principle of Least Privilege
Each IAM role receives only the permissions necessary for its specific
function. This reduces the damage that could occur if an account or
service were compromised.



## Task 13 — IoT Devices, Communication Technologies and IoT Architecture
## IoT Devices
The system uses the following IoT devices in the three zones:
| Device | Purpose |
|---|---|
| Traffic Sensor | Measures traffic flow and congestion |
| Air-Quality Sensor | Measures pollutants and air quality |
| CCTV Camera | Provides visual monitoring for public safety |
| Smart Streetlight | Monitors and controls street lighting |
| Emergency Sensor | Detects emergency events and sends alerts |
Each device sends sensor information to its respective zone controller.

## Communication Technologies
The following communication technologies are used:
| Technology | Use |
|---|---|
| Wi-Fi | Connects nearby IoT devices to a zone controller |
| 5G | Provides high-speed communication for mobile/high-bandwidth devices |
| MQTT | Lightweight messaging between IoT devices/zone controllers and cloud services |
| HTTPS | Secure communication with cloud APIs and dashboards |

## IoT Data Flow
The basic data flow is:
IoT Sensors
→ Zone Controller
→ Secure Network
→ Cloud IoT Gateway
→ Cloud Processing
→ Part 1 Scheduler and Banker's-Algorithm Engine
→ Database/Storage
→ Smart City Operations Dashboard
The zone controller collects sensor data and sends it securely to the
cloud. The cloud processing layer processes the incoming jobs using the
scheduler from Part 1. The Banker's-Algorithm component checks resource
allocation safety before resources are granted.

## Six-Layer IoT Architecture
## Layer 1 — Physical Environment
This layer represents the real-world city environment where events and
measurements occur.
Examples:
- Roads and traffic
- Air quality
- Public spaces
- Street lighting
- Emergency situations

## Layer 2 — Perception/Device Layer
This layer contains the IoT sensors and devices that collect data from
the physical environment.
Examples:
- Traffic cameras
- Traffic sensors
- Air-quality sensors
- Smart streetlights
- Public-safety devices
The devices collect sensor information and send it to the appropriate
zone controller.

## Layer 3 — Gateway Layer
The zone controllers act as IoT gateways.
They collect data from local devices, perform initial processing and
forward the required information to the cloud platform.
The zone controllers also submit sensor-processing jobs to the scheduler
and Banker's-Algorithm engine from Part 1.

## Layer 4 — Network Communication Layer
This layer provides communication between the zone controllers and the
cloud platform.
Technologies include:
- Wi-Fi
- 5G
- MQTT
- TCP/IP
- HTTPS
TLS protects sensitive communication while travelling across the network.

## Layer 5 — Cloud Platform Layer
The scheduler and Banker's-Algorithm engine from Part 1 is explicitly
the Cloud Platform Layer of this deployment.
The engine performs:
- Job scheduling
- Waiting and turnaround calculations
- Resource-allocation safety checking
- Deadlock-safety analysis
Cloud services also provide storage, monitoring and processing for
sensor data.

## Layer 6 — Application Layer
This layer provides services used by city operators and users.
Examples:
- Smart City Operations Dashboard
- Public-safety alerts
- Traffic monitoring
- Environmental monitoring
- Sensor-log analysis
- Scheduling and resource-management services

## IoT Device and Communication Mapping
| IoT Device | Communication Technology | Reason |
|---|---|---|
| Traffic camera | 5G | High bandwidth is suitable for transmitting video and real-time traffic information |
| Air-quality sensor | Zigbee | Low-power communication is suitable for small sensor readings |
| Wearable public-safety device | Bluetooth | Short-range, low-power communication is suitable for a wearable device |
These devices communicate with their local zone controller/gateway,
which forwards relevant information through the Network Communication
Layer to the Cloud Platform Layer.



## Task 14 — Secure IoT Communication
## TLS Protection
TLS 1.3 is used to protect communication between the zone controllers
and cloud services.
For example:
Zone Controller
→ TLS 1.3
→ Cloud IoT Gateway
TLS provides:
- Confidentiality — prevents unauthorized users from reading the data.
- Integrity — helps detect if data is modified during transmission.
- Authentication — verifies the identity of the communicating endpoint.
Public-safety alerts, sensor data and API communication are therefore
protected while travelling across the network.

## Firewall Protection
A network firewall/security group is placed at the cloud network
boundary.
Its main purpose is to allow only required traffic and block
unauthorized network connections.
Example rules:
| Source | Destination | Protocol/Port | Action |
|---|---|---|---|
| Zone Controllers | Cloud IoT Gateway | MQTT/TCP 8883 | Allow |
| Zone Controllers | Cloud API | HTTPS/TCP 443 | Allow |
| Zone-B Subnet | Zone-A Subnet | Any unauthorized traffic | Deny |
| Internet | Private Zone Subnets | Direct access | Deny |
The firewall therefore provides network-level protection and also
maintains the isolation between the three zones.

## Intrusion Detection System
A Network Intrusion Detection System (NIDS) monitors network traffic
for suspicious or malicious activity.
For example, if an attacker repeatedly attempts unauthorized connections
to the cloud gateway, the NIDS can detect the abnormal traffic pattern
and generate a security alert.
The NIDS is used for detection and monitoring, while the firewall is
responsible for enforcing network access rules.

## Secure IoT Communication Flow
The secure communication path is:
IoT Device
→ Zone Controller
→ Firewall/Security Group
→ TLS 1.3
→ Cloud IoT Gateway
→ Cloud Processing Layer
→ Part 1 Scheduler and Banker's-Algorithm Engine
The zone controller authenticates with the cloud service and establishes
a TLS-protected connection. Only permitted network traffic is allowed
through the firewall. The NIDS monitors the traffic for suspicious
activity.

## Security Controls Summary
| Security Requirement | Control |
|---|---|
| Confidential communication | TLS 1.3 |
| Network access control | Firewall/Security Group |
| Intrusion detection | NIDS |
| User access control | RBAC |
| Identity protection | MFA |
| Stored-data protection | Encryption at Rest |
| Minimum permissions | Principle of Least Privilege |



## Task 14 — Cloud-IoT Threats and Mitigations
The following threats are specifically relevant to the Smart City
Cloud-IoT platform and the scheduler and Banker's-Algorithm engine
from Part 1.

## 1. IoT Device Compromise
Threat:
An attacker could compromise a traffic sensor, environmental sensor or
other IoT device and use it to send false or malicious data to the
zone controller.
Mitigation:
Use device authentication with unique device credentials or certificates
and allow only authenticated devices to connect to the IoT gateway.

## 2. Denial-of-Service (DoS) Attack
Threat:
An attacker could send a large number of requests to the cloud services,
making the platform unavailable to legitimate zone controllers.
Mitigation:
Use rate limiting and a firewall/WAF to restrict excessive traffic and
block suspicious requests. Monitoring can also detect abnormal traffic
patterns.

## 3. Man-in-the-Middle (MITM) Attack
Threat:
An attacker could attempt to intercept or modify sensor data or
public-safety alerts while they travel between a zone controller and
the cloud.
Mitigation:
Use TLS 1.3 for communication between zone controllers and cloud
services. TLS provides encrypted and authenticated communication.

## 4. Unauthorized Cloud Access
Threat:
A compromised user account could be used to access sensor data,
configuration or the scheduler services without authorization.
Mitigation:
Use MFA and RBAC with the principle of least privilege. Users receive
only the permissions required for their role.

## 5. Cross-Zone Network Attack
Threat:
A compromised Zone-B system could attempt to directly access
Zone-A resources.
Mitigation:
Use separate private subnets and firewall/security-group rules that
deny unauthorized traffic from the Zone-B subnet to the Zone-A subnet.

## Part 1 Engine Protection
The scheduler and Banker's-Algorithm engine from Part 1 is placed in
the protected Cloud Platform Layer. Authentication, least-privilege
access, network isolation, TLS and monitoring reduce the risk of an
attacker reaching or manipulating the engine.


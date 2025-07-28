# Lab-NetworkProgramming

# Lab 03 – Linux Network Programming

This lab was developed as part of the *Mobile and Sensor Networks* course at Politecnico di Torino. The focus was on implementing UDP and TCP client-server communication in Python and analyzing latency under various conditions. Conducted in a team (Group 05).

---

## 🎯 Objectives

- Build basic client-server applications using UDP and TCP sockets
- Capture and analyze packets with Wireshark
- Simulate packet loss and observe behavior differences
- Measure round-trip time (RTT) using timestamps
- Compare application-level RTT with ping results

---

## 🛠️ Tools and Technologies

- Python 3 (socket programming)
- Wireshark
- Linux terminal (ifconfig, tc)
- RTT testing with timestamp analysis

---

## 📁 Files

- `lab_03_group_05.pdf`: Full report
- `udp_client.py` and `udp_server.py`: Basic UDP communication
- `tcp_client.py` and `tcp_server.py`: Basic TCP communication
- `rtt_client.py` and `rtt_server.py`: RTT measurement over TCP

---

## 👥 Group Members

- Valerio Collina  
- Ammar Hussein  
- Md Ismail Hossain  
- Md Ataur Rabby

---

## 📌 Notes

TCP and UDP were compared under normal and lossy conditions (using tc to simulate 20–30% packet loss). RTT was calculated at application level and validated against system-level ping output.

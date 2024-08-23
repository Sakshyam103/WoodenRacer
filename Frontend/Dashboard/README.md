[//]: # ([//]: # &#40;# React + Vite&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;Currently, two official plugins are available:&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;- [@vitejs/plugin-react]&#40;https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md&#41; uses [Babel]&#40;https://babeljs.io/&#41; for Fast Refresh&#41;)
[//]: # ()
[//]: # ([//]: # &#40;- [@vitejs/plugin-react-swc]&#40;https://github.com/vitejs/vite-plugin-react-swc&#41; uses [SWC]&#40;https://swc.rs/&#41; for Fast Refresh&#41;)
[//]: # ()
[//]: # ()
[//]: # (# WoodenRacer)

[//]: # ()
[//]: # (## Overview)

[//]: # ()
[//]: # (This project facilitates communication between a computer and a wooden car using two radios via USB. It ensures simultaneous telemetry sending and receiving between remote controller class and dashboard using Flask. The telemetry includes:)

[//]: # ()
[//]: # (- Velocity)

[//]: # (- Braking force)

[//]: # (- Throttle)

[//]: # (- Steering angle)

[//]: # (- Slip angle)

[//]: # (- Automatic function)

[//]: # ()
[//]: # (The wooden car maintains these data to move the cat and simultaneously receives sensor values &#40;eg., from speed sensors, throttle position sensors, steering position sensors&#41;. These values are then sent back to the remote controller using another radio and displayed on the dashboard.)

[//]: # ()
[//]: # (## Features)

[//]: # ()
[//]: # (- Real-time telemetry transmission and reception.)

[//]: # (- Dashboard for visualizing and controlling car telemetry.)

[//]: # (- Simultaneous data sending and receiving via radios using UART protocol.)

[//]: # (- Data display of both sent telemetry and received sensor values.)

[//]: # ()
[//]: # (## Requirements)

[//]: # ()
[//]: # (- Python 3.x)

[//]: # (- pyserial)

[//]: # (- Flask)

[//]: # (- Other dependencies as needed)

[//]: # ()
[//]: # (## Installation)

[//]: # ()
[//]: # (1. Clone the repository:)

[//]: # (   ```sh)

[//]: # (   git clone https://github.com/tenbergen/WoodenRacer.git)

[//]: # (   cd Frontend/Dashboard)

[//]: # (   npm run dev)

[//]: # (   cd ..)

[//]: # (   python3 RC.py)

[//]: # (   python3 AV.py)
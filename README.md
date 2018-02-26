# Object Detection at the Edge

## Prerequisites
Install the following tools on your Edge device: [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/overview/). Use the following links to help you:
* [Docker Community Edition installation](https://www.docker.com/community-edition#/download)
* [Docker Compose installation](https://docs.docker.com/compose/install/)

My Edge device is currently running Fedora 27, with the following versions of the abovementionned packages:
* Docker version 18.02.0-ce, build fc4de44
* docker-compose version 1.19.0, build 9e633ef

We use IP cameras from [SV3C](http://www.sv3c.com/), more specifically the POE models (that can do 1080p): http://www.sv3c.com/POE-IP-Camera.html

## Building the docker image
1. Clone this repository locally: `git clone https://github.com/inc0/video_detection`
2. Make sure [Docker](https://www.docker.com/) is running: `sudo systemctl start docker`
3. Build the Docker image: `cd video_detection && docker build -t streamapp .`

**Note:** you need to use `streamapp` as the name of the Docker container you are building as it is used in the [`docker-compose.yml`](./docker-compose.yml) file

## Running the Object Detection on the Edge device
*Note:* unless you have installed Docker and performed [these post-installation steps](https://docs.docker.com/install/linux/linux-postinstall/), you will need to use `sudo` to use `docker-compose`. For some reason, it does not find the `docker-compose` executable and I have to use the full path to it, i.e. `sudo /usr/local/bin/docker-compose up` (to be investigated later, or maybe a reboot will solve it).

1. Set-up the IP camera following the online [User Guides](http://www.sv3c.com/Instruction-and-Software-For-H-264-POE-and-Wired-IP-Camera-L-series-.html)
2. Take note of the IP address assigned to the camera

*We use an environment variable to pass the IP address of the camera to the container that will capture the video stream. The name of the variable is `IP_CAMERA`.*
3. Start the Object Detection service
```
sudo IP_CAMERA=192.168.0.130 /usr/local/bin/docker-compose up
```
4. Open a broswer at http://0.0.0.0:5000 to see the results


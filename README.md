# Object Detection at the Edge

## Prerequisites
Install the following tools on your Edge device: [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/overview/). Use the following links to help you:
* [Docker Community Edition installation](https://www.docker.com/community-edition#/download)
* [Docker Compose installation](https://docs.docker.com/compose/install/)

My Edge device is currently running Fedora 27, with the following versions of the abovementionned packages:
* Docker version 18.02.0-ce, build fc4de44
* docker-compose version 1.19.0, build 9e633ef

We use IP cameras from [SV3C](http://www.sv3c.com/), more specifically the POE models (that can do 1080p): http://www.sv3c.com/POE-IP-Camera.html

## Getting ready
1. Clone this repository locally: `git clone https://github.com/inc0/video_detection`
2. Make sure [Docker](https://www.docker.com/) is running: `sudo systemctl start docker`
3. Put yourself in the cloned folder: `cd video_detection`

**Note:** you do not need to need to build any Docker container. It will be built automatically for you if not yet available. See the `build` instruction in the [`docker-compose.yml`](./docker-compose.yml) file.

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

# Notes about running on Clear Linux

It is possible to run the same set-up on Clear Linux. Unfortunately, it is **not** possible to use Clear Containers for this yet (a bug has yet to be filed).

## Prerequisites
Same as for Fedora 27 (or any other OS really), install [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/overview/). Use the following guides to help you:
* [Installing Clear Containers 3.0 on Clear Linux](https://github.com/clearcontainers/runtime/blob/master/docs/clearlinux-installation-guide.md)
* Install `docker-compose`:
```
$ sudo curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-compose-`uname -s`-`uname -m` -o /usr/bin/docker-compose
$ sudo chmod +x /usr/bin/docker-compose
```

Because of the current issue with Clear Containers 3, we have to change the default behaviour of Docker when running in Clear Linux (bare metal). The background is that, by default, it will pick the Clear Containers 3 runtime (`cc-runtime`) when running bare-metal so we need to force the system to **not** do that.

One way to achieve this (not sure whether it's the best way) is to modify the `docker.service` file (`/lib/systemd/system/docker.service`) and change the `ExecStart` line to this:
```
ExecStart=/usr/bin/dockerd --storage-driver=overlay2 --default-runtime=runc
```

Now reload and restart the daemon:
```
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

Verify that the `runc` runtime is being used:
```
sudo docker info | grep Run
```

You are now ready to continue from [Running the Object Detection on the Edge device](#running-the-object-detection-on-the-edge-device)

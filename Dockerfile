FROM tensorflow/tensorflow:latest-py3

RUN apt-get update && apt-get -y install git python-opencv wget protobuf-compiler
RUN pip3 install Flask opencv-python redis ipython

RUN mkdir /mobilenet
RUN git clone https://github.com/tensorflow/models.git
RUN wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2017_11_17.tar.gz && \
    tar -xvzf ssd_mobilenet_v1_coco_2017_11_17.tar.gz -C /mobilenet

RUN mkdir /streamapp
RUN cp -R models/research/object_detection /streamapp
RUN cd /streamapp && protoc object_detection/protos/*.proto --python_out=.
WORKDIR /streamapp
COPY . .

EXPOSE 5000
CMD python3 app.py

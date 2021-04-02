FROM pytorch/pytorch:1.6.0-cuda10.1-cudnn7-devel

ENTRYPOINT ["echo", "hello"]

WORKDIR /mmdetection

ADD ./mmdetection

RUN apt install python3.7.4 -y
RUN vim 

EXPOSE 8080
CMD ["/bin/bash"]

## Object Detection in Drone Dataset (contain UI)

### My Environment
- OS : Ubuntu 18.04.5
- GPU : NVIDIA RTX 2070 super
- CUDA : 10.2

### Reference
- <a href='https://github.com/ultralytics/yolov5'>yolov5</a>

- <a href='https://github.com/open-mmlab/mmdetection'>mmdetection</a>



### weight file

- yolov5 : weights/drone_survivor.pt 🥇
- cascade rcnn : https://drive.google.com/file/d/1mXANwNMbQU7tmmmhZ81dFaIRvXU6rDQL/view?usp=sharing
- faster rcnn : https://drive.google.com/file/d/1mXANwNMbQU7tmmmhZ81dFaIRvXU6rDQL/view?usp=sharing
- retina net : https://drive.google.com/file/d/1mXANwNMbQU7tmmmhZ81dFaIRvXU6rDQL/view?usp=sharing

⚠️ weights/drone_survivor.pt  = yolov5 weight model


⚠️ If you use other model(Cascade RCNN, RetinaNet etc.), enter <a href='https://github.com/open-mmlab/mmdetection'>this page</a>


### How to do?

```
$ git clone https://github.com/winston1214/Object_Detection_Drone && cd Object_Detection_Drone
```
```
$ pip install -r requirements.txt
```
```
$ python3 ui2.py
```

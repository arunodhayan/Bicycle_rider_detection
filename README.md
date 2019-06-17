# Bicycle_rider_detection
Transfer learning to detect Bicycle rider detection


## Process
    1.Collect dataset
    2.Label the image using Labelimg a python anootation tool
    3.Tranfer learning using Tensorflow Framework
    
## Dataset Annotation and preprocessing datasets
    The dataset was annotated using LabelImg
    The xml files will be generated
    Use xmltocsv.py to convert the xml files to csv
    Create Tfrecords using tfrecords.py
    create a label map named .pbtxt
    
 ## Before Training
   Now the preprocesing is done 
  clone this repo https://github.com/tensorflow/models.git
  1.Then perform these below steps before going in to actual training
      
      git clone https://github.com/cocodataset/cocoapi.git
      cd cocoapi/PythonAPI
      make
      cp -r pycocotools <path_to_tensorflow>/models/research/
   2.Manual protobuf compile
       
       # From tensorflow/models/research/
        wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
        unzip protobuf.zip
        # From tensorflow/models/research/
        ./bin/protoc object_detection/protos/*.proto --python_out=.
        # add libraries to pythonpath
         # From tensorflow/models/research/
           export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
           you can add it as a new line to the end of your ~/.bashrc file, replacing `pwd` with the absolute path of                      tensorflow/models/research on your system.
        #Testing
        python object_detection/builders/model_builder_test.py
  ## Training      
   Here i had use faster_rcnn a pretrained model
   you can find a pretrained model in                      
   models/research/object_detetction/samples/config/faster_rcnn_inception_v2_coco.config
   Edit these lines
        
        Line 10 : num_classes=1
        Line 107: change the checkpoint, Download a model ckpt from model zoo
        Line 122 and 124: change the file path for train.record and .pbtxt which you created in data processing
        Line 128: no of examples= no of training images 
        Line 136 and 138 : change the file path for test.record and .pbtxt which you created in data processing
        save the file 
  ## Run the training
since the new model_main.py ran in to error i had used previous train.py
       
        python2 train.py ----logtostderr --train_dir=training/ --
        pipeline_config_path=samples/configs/faster_rcnn_inception_v2_coco.config
        
 ## Testing
    To test image use object.py file
    To test video use object_video.py file 
    if error occus util cant be found 
    cd .. move to research folder
      export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim -- try to run this 
      then python2 object_detection/object.py
        
    The work was inspired from https://pylessons.com/Tensorflow-object-detection-step-by-step-custom-object-detection/      

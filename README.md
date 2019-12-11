# 5G-Utility-Pole-Planner (Team 14)

## Team Members

- Yanyu Zhang (U47793163)
- Luxuan Qi (U29067565)
- Zhou Fang (U03663101)

<p align="center">
  <a href="https://docs.google.com/presentation/d/1qWq742s4NI8pn1bmFl8gep5iJmCOW43pqanhG7Z6wek/edit?usp=sharing">Sprint1</a>
</p>

<p align="center">
  <a href="https://docs.google.com/presentation/d/1_AwGJDqD3ICkyTWdblvogblYmDKTAUlKJ4mJW6xaTWo/edit?usp=sharing">Sprint2</a>
</p>

<p align="center">
  <a href="https://github.com/zhangyanyu0722/5G-Utility-Pole-Planner/blob/master/result/A1_14.pdf">Poster</a>
</p>



## Product Definition

### Project Mission
- In order to help company to install 5G equipments on untility Poles, our first aim is to build our first dataset by Google street imagery. With machine leaning, we will import the dataset and analyse the poles in every image so that we can build a 2D model of the whole neighbourhood. At the same time, our team members are going to use the knowledge of 5G and make an abstraction of each equipment as to build the final model.

### Target User(s)
- 5G operator
- 5G maintenance company

### User Stories

- I, the 5G operator, want to identify the poles in the picture and get their coordinates.
- I, the 5G operator, want to know the distribution of poles on the street.
- I, the 5G operator/maintenance company, want to know how to achieve full coverage of 5G signals with a minimum of 5G devices.

### MVP

1. Detect the poles from the pictures.
2. Label poles on a 2D map in a small area.
3. Reasonably distribute 5G equipment.

### How it works

1. Get an access to Google Api and utilize it to crawl the pictures from Google Street View. 
2. Use computer vision to detect poles from every picture if there is any.
3. Build a map that shows how the poles scattered around the area we choose.
4. Make a module for each 5U Utilities, including its coverage area.
5. Combine 3 & 4 to reach the final design.

## Product Survey

### Existing similar products
1. Using Deep Learning to Identify Utility Poles from Google Street View Images
   - research paper available [here](https://github.com/zhangyanyu0722/5G-Utility-Pole-Planner/blob/lqi/thesis_pole.pdf).
   - Advantages:
      - using deep learning based method.
      - combine the state-of-the-art DL object detection algorithm and a modified brute-force-based line-of-bearing measurement method.
      - both the average precision and the overall accuracy are around 0.78.
      - 47% and 79% of estimated locations of utility poles are within 5 m, and 10 m buffer zones
   - Disadvantages:
      - only one method being used for each task of detection.
      - some google street view images are very old.
      - a large amount of training dataset is needed to achieve an acceptable accuracy with the Retina-101.
      - a lot of utility poles do not have crossarms used to detect.
   - Approach:
      - process the extracted road GIS dataset.
      - get images through google street view.
      - use a training dataset to train the DL algorithm and a test dataset to access the performance.
2. Image Analysis-based Automatic Utility Pole Detection
   - research paper available [here](https://github.com/zhangyanyu0722/5G-Utility-Pole-Planner/blob/lqi/paper.pdf).
   - Advantages:
      - the algorithm is more robust compared to others.
      - the algorithm can detect leaning or bent poles as well.
      - detect poles in complex surroundings.
   - Disadvantages:
      - still exist incorrect test results.
      - need to improve handling of weak edges.
   - Approach:
      - extract keyframes from the video.
      - extract 2D shapes of poles and create a shape-based template.
      - detect a pole with any degree of leaning.
      - algorithm:mean-shift segmentation->block-oriented quadrilateral extraction->orientation-based spatial clustering of near-trapeziums->context-based detection of utility pole


## System Design

### Major Components
- Street View Static Api
- Trained model/algorithm

### Technology Selection
- Street View Static Api
   - get the images of the set coordinate points.
   - get images of different angles from the same coordinate point.
   - set the size of image.
- Trained model/algorithm
   - Python
       - easy to use
       - very convenient when learning machine

## What We Have Done

### Web Design

- Use Django to make web pages.
- Connect to the Google Map api and click anywhere on the map to get the coordinates of that point.
- Enter the latitude and longitude coordinates of the upper left and lower right corners of the selection area on the web page.
- Click the Submit button to download the image of the area from the google static street view api to a local folder.
- Use a trained model to identify whether a pole is included in the picture, and use MATLAB to mark the pole on the map and distribute 5G equipment.
- Click the Result button to view the results on the web page.   

<img src="https://github.com/zhangyanyu0722/5G-Utility-Pole-Planner/blob/lqi/webpage.png" width="400" />

### Trained Model
1. For the poles' detection, our fundamental purpose is to detect whether poles exist in pictures or not. The methods are basic CNN and Mark-RCNN. After comparison, Mark-RCNN has the higher accuracy, but has lower speed than the basic CNN. In this demo, we used the basic CNN with the increased dataset, which contains 3,000 photos. The results are showing as following:
<p float="middle">
  <img src="https://github.com/zhangyanyu0722/5G-Utility-Pole-Planner/blob/master/result/loss_4.png" width="400" />
  <img src="https://github.com/zhangyanyu0722/5G-Utility-Pole-Planner/blob/master/result/acc_4.png" width="400" />
  
Model link: "https://github.com/zhangyanyu0722/5G-Utility-Pole-Planner/blob/master/result/poles_and_nonpoles_3.h5"

2. We labled about 100 pictures with poles, and used those pictures in the Mark-RCNN, then trained with 25 epoches, and the result is showing below:
<p align="middle">
  <img src="https://github.com/zhangyanyu0722/5G-Utility-Pole-Planner/blob/master/result/mrcnn.png" width="300">
  
Model link: "https://drive.google.com/file/d/1Fk6RSlX70yz-rzwgo4dwI-ZkqjVCS0Le/view?usp=sharing"

  
  

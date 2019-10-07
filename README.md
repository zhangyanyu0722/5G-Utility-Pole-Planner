# 5G-Utility-Pole-Planner (Team 15)

## Team Members

- Yanyu Zhang (U47793163)
- Luxuan Qi (U29067565)
- Zhou Fang (U03663101)

## Product Definition

### Project Mission
  In order to help company to install 5G equipments on untility Poles, our first aim is to build our first dataset by Google street imagery. With machine leaning, we will import the dataset and analyse the poles in every image so that we can build a 2D model of the whole neighbourhood. At the same time, our team members are going to use the knowledge of 5G and make an abstraction of each equipment as to build the final model.

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
### Patent analysis

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

### Test programs

## What We Have Done

1. We have got the access to Google Map Api so that we were able to download the pictures from Google Street View, though it gave us a limit of 2000 per day.
2. Found a labeled dataset of telephone poles, containing 98 images.

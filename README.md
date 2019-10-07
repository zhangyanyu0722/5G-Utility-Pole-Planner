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
1.DetectUtilityPoles

### Patent analysis

## System Design

### Major Components

### Technology Selection

### Test programs

## What We Have Done

1. We have got the access to Google Map Api so that we were able to download the pictures from Google Street View, though it gave us a limit of 2000 per day.
2. Found a labeled dataset of telephone poles, containing 98 images.

# facebook_profile_analysis
Reads and visualizes data downloaded from the 'Download Your Information' feature in Facebook (https://www.facebook.com/settings?tab=your_facebook_information )

To get started, go to the above URL and download all your information in JSON export format. Next, once your information is prepared, download and unzip the archive into a new directory. You can create a FacebookProfile object by using the directory path of the unzipped archive root, which will allow the object to be used like a dictionary of the entire archive.

This repo is currently a collection of scripts that will build over time. I want to use this to visualize the analytics of my Facebook profile, including activity metrics, interaction types, and potentially machine learning projects based on the text in my profile.

## Goals

* Access my data in a programmatic way
* Compute analytics about my profile
* Visualize these analytics

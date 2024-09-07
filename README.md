# Road-Seg
Enhancing road segmentation model for Asphalt edge detection
(This project was done as a part of my internship at Avular Innovations,Eindhoven,Netherlands)


# About

This project investigates different out-of-distribution
generalization strategies primarily using data augmentation to
implement a binary segmentation model. The model aims to
detect the road edge while ensuring consistent segmentation
performance in different weather conditions, camera properties,
and image perspectives. Out-of-distribution (OOD) generalization
denotes the capability of a model to effectively and accurately pre-
dict data that deviates from the distribution encountered during
its training phase. Achieving adeptness in OOD generalization is
essential for ensuring the model’s reliability and effectiveness
in real-world deployment scenarios. Data augmentation was
adopted and tested through three different experiments. The first
experiment analyzes how our model architecture generalizes to
OOD data during testing with the help of data augmentation. The
second experiment studies the effect of various data augmentation
transforms on the road edge segmentation performance. The
third experiment explores the effectiveness of employing transfer
learning for enhancing road edge segmentation. Our findings
show that data augmentation enhances the model’s performance
by increasing its robustness to various operating conditions, while
also promoting generalization to out-of-distribution data.
For more information about the implementation, please refer to the report [here](1820230-Internshipreport.pdf)


<div  align="center">    
  <img src="https://github.com/bratjay01/Road-Seg/blob/main/Final_prediction_1.jpeg" width="1000" height="200" />
  <img src="https://github.com/bratjay01/Road-Seg/blob/main/Final_prediction_2.jpeg" width="1000" height="200" />   
</div>

<div  align="center">    
  <img src="https://github.com/bratjay01/Road-Seg/blob/main/Final_prediction_3.jpeg" width="1000" height="200" />
  <img src="https://github.com/bratjay01/Road-Seg/blob/main/Final_prediction_4.jpeg" width="1000" height="200" />   
</div>

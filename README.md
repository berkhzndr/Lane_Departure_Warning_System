# Python Plays Grand Theft Auto 5 - Reboot

<p align="center"><img src="_media/charles.webp"></p>

This is a reboot of the project from 2017, but with a whole new approach. This time, instead of collecting data by hand and training a classification model, we opted to create a whole new system for the data collecting, training and playing, and to do all of that live. Our models are now using regression (with other output types being still possible), training data is collected automatically and we stream models during their training phase so anyone can join and watch the progress.

Our AI, besides having multiple alter-egos (models), is still called **Charles**, like in 2017.

For a full explanation, refer to the [`System`](project_info/system.md) page, but for a quick summary - we’re using a central server that all other parts connect to. The [`Data Collectors`](project_info/system.md) run in separate GTA5 instances and our NPCs are collecting and [`Balancing`](project_info/data_balancing.md) the data, which is sent through the [`Server`](project_info/system.md) to the [`Trainer`](project_info/system.md). The [`Trainer`](project_info/system.md) buffers these data, trains the model and updates the [`Player`](project_info/system.md). The [`Player`](project_info/system.md) is using the [`Dual-Camera`](project_info/cameras.md) system to play so we can watch the 3rd person camera (also called cinematic camera) while the model is fed the [`Hood Camera`](project_info/cameras.md).

For more information, refer to these other pages:
- this page - main page with the project progress
- [`System`](project_info/system.md) - describing how all parts are working together to train and inference the models
- [`Cameras`](project_info/cameras.md) - how we created multiple cameras
- [`Convcam`](project_info/convcam.md) - what the Convcam is and how we use it
- [`Data Balancing`](project_info/data_balancing.md) - how we are balancing regression data
- [`NPCs`](project_info/NPCs.md) - our custom NPCs playing in the GTA5 to collect data automatically
- [`Purpose`](project_info/purpose.md) - a way to let the model “know” where to drive
- [`Storage and Buffer`](project_info/storage_buffer.md) - how are we managing the training data and why random batches are important
- [`Unstuck`](project_info/unstuck.md) - how to make the car not be stuck anywhere
- [`Xception`](project_info/xception.md) - the first CNN backbone architecture used
- [`InceptionResNetv2`](project_info/inceptionresnetv2.md) - the second, more successful, CNN backbone architecture used
- [`Tensorboard logs`](tensorboard_logs) - all of our Tensorboard logs for all of the trained models
- [The Original Project From 2017](original_project)
- [`model_0001_xception`](model_0001_xception) - the first logged [`Xception`](project_info/xception.md) model, [`Balancing_v1`](project_info/data_balancing.md)
- [`model_0002_xception`](model_0002_xception) - trying [`Balancing_v2`](project_info/data_balancing.md) and a custom model
- [`model_0003_xception`](model_0003_xception) - [`Balancing_v3`](project_info/data_balancing.md) and back to a standard model
- [`model_0004_inceptionresnetv2`](model_0004_inceptionresnetv2) - trying a bigger model - [`InceptionResNetv2`](project_info/inceptionresnetv2.md)
- [`model_0005_inceptionresnetv2`](model_0005_inceptionresnetv2) - transfer-learning attempt
- [`model_0006_inceptionresnetv2`](model_0006_inceptionresnetv2) - added stacked images
- [`model_0007_inceptionresnetv2`](model_0007_inceptionresnetv2) - trying a history inputs
- [`model_0008_irv2_data_td`](model_0008_irv2_data_td) - history with recurrent layers
- [`model_0009_irv2_cr_tl`](model_0009_irv2_cr_tl) - history with recurrent layers with transfer-learning
- [`model_0010_irv2_tcb`](model_0010_irv2_tcb) - dual-backbone [`InceptionResNetv2`](project_info/inceptionresnetv2.md)
- [`model_0011_x_tcb`](model_0011_x_tcb) - dual-backbone [`Xception`](project_info/xception.md)
- [`model_0012_regnet`](model_0012_regnet) - TBA

<br/>
<br/>

# Stream and current stream layout:
The progress is being streamed on Twitch: [https://www.twitch.tv/sentdex](https://www.twitch.tv/sentdex). Below we keep a list of dates and streamed models.

Stream's layout consists of:
![layout.jpg](_media/layout.jpg)  
- top-left tile is the 3rd person camera of the car driving, the main camera to observe Charles
- this main tile, in its lower-right corner, shows the current model and when it's been created
- top-right tile called [`Hood Camera`](project_info/cameras.md) is exactly what the models "see" - the input to the convolutional backbone of the model
- middle-right tile called [`Convcam`](project_info/convcam.md) shows the reshaped output of the CNN backbone and lets us observe how the CNN part trains
- bottom-right tile called [`Player Console`](project_info/system.md) shows current driving predictions along with additional information
- bottom-middle tile called [`Server/Trainer Console`](project_info/system.md) shows training progress along with some basic training information
- bottom-left tile called [`Tensorboard`](tensorboard_logs) shows the loss of the training process

<br/>
<br/>

# Driving examples:
<a href="https://clips.twitch.tv/GiftedRespectfulParrotGOWSkull-17xBRPKKdDvr_3Wf"><img src="_media/AT-cm_qfUNoNe8QUTyinQ76_91nw.jpg" width="49.4%"></a>&nbsp;
<a href="https://clips.twitch.tv/HealthyRichWeaselPlanking-6oB5PoNygm5ikonY"><img src="_media/AT-cm_F6V9NuqAeT6DcoJuYpKJ2A.jpg" width="49.4%"></a>

<br/>
<br/>

# Model list:

- [The Original Project From 2017](original_project) - how this started
- [`model_0001_xception`](model_0001_xception) - the first logged [`Xception`](project_info/xception.md) model, [`Balancing_v1`](project_info/data_balancing.md)
- [`model_0002_xception`](model_0002_xception) - trying [`Balancing_v2`](project_info/data_balancing.md) and a custom model
- [`model_0003_xception`](model_0003_xception) - [`Balancing_v3`](project_info/data_balancing.md) and back to a standard model
- [`model_0004_inceptionresnetv2`](model_0004_inceptionresnetv2) - trying a bigger model - [`InceptionResNetv2`](project_info/inceptionresnetv2.md)
- [`model_0005_inceptionresnetv2`](model_0005_inceptionresnetv2) - transfer-learning attempt
- [`model_0006_inceptionresnetv2`](model_0006_inceptionresnetv2) - added stacked images
- [`model_0007_inceptionresnetv2`](model_0007_inceptionresnetv2) - trying a history inputs
- [`model_0008_irv2_data_td`](model_0008_irv2_data_td) - history with recurrent layers
- [`model_0009_irv2_cr_tl`](model_0009_irv2_cr_tl) - history with recurrent layers with transfer-learning
- [`model_0010_irv2_tcb`](model_0010_irv2_tcb) - dual-backbone [`InceptionResNetv2`](project_info/inceptionresnetv2.md)
- [`model_0011_x_tcb`](model_0011_x_tcb) - dual-backbone [`Xception`](project_info/xception.md)
- [`model_0012_regnet`](model_0012_regnet) - TBA

<br/>
<br/>


<h1>Introduction</h1>
<p>This repository contains all the necessary Artificial Intelligence Model code and examples to work with them for Beamline for Schools Competition 2023 submission of team Sound waves, representing Pakistan.</p>
<h2>Overview &amp; Caution</h2>
<p>In our paper, we mentioned using YAMNet from Google, that&rsquo;s why, we have loaded the pretrained YAMNet model from Tensorflow Hub and by default allowed the parameters/weights to be trained but we advise to change it to False to achieve better results.</p>
<p>If you encounter any issues kindly raise an issue on this repository and it&rsquo;ll be fixed in 24 hours.</p>
<h2>How to load the model?</h2>
<p>Go to the <strong>import</strong> folder and import all the required libraries and then go to the <strong>model</strong> folder and import the learn_model.py file into your working file and you&rsquo;ll have the YAMNet model.</p>
<h2>How to train the model?</h2>
<p>You can either use our train.py file to start training your model on your dataset or write your own training loop.</p>
<h2>Denoising the audio</h2>
<p>You can visit the <strong>denoise</strong> folder and see the denoise spec.py file which can be used for denoising your audio.</p>
<h2>Creating audio spectrogram</h2>
<p>Visit the <strong>audio_spectrogram</strong> folder and use the gram.py file to create your spectrogram.</p>
<h2>What&rsquo;s the notebook folder</h2>
<p>Notebook folder contains easy to use examples of our concept by anyone using an interactive python notebook aka Jupyter Notebook. You can either run on your computer if you have GPUs otherwise kindly use <a href="https://colab.research.google.com/"Google Colab</a>.</p>
<h2>Do we use QCNN?</h2>
<p>Quantum Convolutional Neural Networks (QCNNs) are a type of quantum machine learning algorithm that can be used to analyze complex data sets. In the context of particle physics, QCNNs can be applied to analyze the audio spectrograms of particle interactions.

Compared to classical QNNs, QCNNs have the potential to offer significant advantages when analyzing large and complex data sets. Firstly, QCNNs can perform parallel computations, which can significantly speed up the analysis of large data sets. Secondly, QCNNs can potentially leverage the power of quantum entanglement to extract more information from the data.

In the case of analyzing audio spectrograms of particle interactions, the data set can be very large and complex. The spectrograms can contain a vast amount of information, and extracting meaningful insights from them can be challenging. QCNNs, due to their potential to perform parallel computations and leverage quantum entanglement, can potentially provide better results than classical QNNs.

However, it is important to note that QCNNs are still in the early stages of development, and their potential advantages over classical QNNs are not yet fully understood. You can find the code for QCNN in our notebook folder in the repo. </p>
<h2>Why we don&rsquo;t have a dataset?</h2>
<p>We don&rsquo;t have a dataset for our project yet so we didn&rsquo;t add any dataset by default in our repository but you can audio datasets of your choice, few examples are UrbanAudio8K, Audioset and more and then perform interferences using our notebook.</p>
<h2>Citations</h2>
<p>The code in this repository originally written by <strong>@sleepingcat4</strong> and copyrighted under MIT Licence for distribution.
And it was written following updated Tensorflow documentation.</p>

1. https://www.tensorflow.org/hub/tutorials/yamnet
2. https://www.tensorflow.org/hub/tf2_saved_model

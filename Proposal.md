# 597Project Proposal
After this semester’s study, I get some basic knowledge about machine learning. As one part of key knowledge in unsupervised learning, deep learning become a hot topic in the world. It gets a state of the art results on many fields, such as computer vision and natural language processing.Compare with problems in computer vision, it still has a long way for people to catch on programming language and biological information problem in deep learning.  
Most important topic in Bioinformatics focus on how to predict the next DNA/RNA sequence. I want to use some deep learning knowledge to help us predict the next label in sequence of DNA. Machine learning is widely used to analyze biological sequence data. Non-sequential models such as SVMs or feed-forward neural networks are often used although they have no natural way of handling sequences of varying length. As we know, deep learning is a branch of machine learning based on a set of algorithms that attempt to model high-level abstractions in data by using multiple processing layers, with complex
structures or otherwise, composed of multiple non-linear transformations. [wiki] Instead of feature selection, I could use deep learning to help us find the appropriate data feature and do some prediction. 

Our goal is based on the paper Convolutional LSTM Networks for subcellular Localization of Proteins, and I try to use different model and
language (lua) to achieve it.

In general, I try to use a long short-term memory (LSTM) model (One kind of recurrent neural networks) on the designed to handle sequences. I will analyze it and predict the subcellular location of proteins given only the protein sequence with high accuracy outperforming current state of the art algorithms. Due to I still try to figure out some of dataset meaning and I could modify some steps and goals depend on our study on this field.

Lua : Lua is a powerful, fast, lightweight, embeddable scripting language.
Lua combines simple procedural syntax with powerful data description constructs based
on associative arrays and extensible semantics. Lua is dynamically typed, runs by
interpreting bytecode for a register-based virtual machine, and has automatic memory
management with incremental garbage collection, making it ideal for configuration,
scripting, and rapid prototyping.

Reference:
[1] Babak Alipanahi1,2,6, Andrew Delong1,6, Matthew T Weirauch3–5 & Brendan J
Frey1–3, Predicting the sequence specificities of DNA- and RNA-binding proteins by
deep learning, Nature
[2] Søren Kaae Sønderby1* Casper Kaae Sønderby1* Henrik Nielsen3,Ole Winther1,2,
Convolutional LSTM Networks for Subcellular Localization of Proteins
[3] Amino Sequence kernel description. https://en.wikipedia.org/wiki/Proteinogenicaminoacid.Accessed :
2010 − 09 − 30.
[4] Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly learning to align and translate. arXiv preprint
    arXiv:1409.0473, 2014.
[5] Ronan Collobert, Koray Kavukcuoglu, and Cl ́ement Farabet. Torch7: A matlab-like environment for machine learning. In BigLearn, NIPS Workshop,
number EPFL-CONF-192376, 2011.

# BWT Exploration
## What is the BWT
The Burrows-Wheeler Transform (BWT) is a lossless organization algorithm that allows for clustering identical data together such that methods like Run Length Encoding (RLE) can be used to compress large data sources into more managable sizes.

Importantly, in bioinformatics, the BWT of a reference sequence can be used as a suffix array to quickly align an unknown sequence.

---
## What is this repo about?
Despite having no formal educational background in computer science, I've been interested in the intricacies of algorithmic data structures and process for a while. Python is currently my strongest language and as such implementing a widely used data structure and method (examples include BWA and Bowtie) used on that data structure will prove insightful. Additionally, I feel that I've reach a point in my career where the algorithms that interest me the most may be implemented in Python, they would be vastly more performant if implemented in a compiled language in order to be of practical use.

---
## Installation
* Create a virtual environment
* Install in developer mode from the repo directory 
  > `pip install -e .`

---
## Testing
Tests are written using pytest in a test driven development cycle. Prior to a new function being written, a test should be written up. Tests directory structure should reflect a 1:1 relationship with `*.py` files in `lib`

---
## Resources
This set of medium articles have been immenensly helpful in understanding how alignment can be achieved using the BTW:
* [BTW Part1](https://medium.com/@mr-easy/burrows-wheeler-alignment-part-1-eb93057bfff5)  
* [BWT Part2](https://medium.com/@mr-easy/burrows-wheeler-alignment-part-2-89e08729822a)
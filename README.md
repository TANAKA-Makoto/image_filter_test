# image_filter_test
## dependence
opencv-python
## useage
require either `--append_dst` or `--normal_dst`.  
`--append_dst` is folder path.  
`--normal_dst` is folder path and file name.
### Gaussian
`./Gaussian.py 'source_path' (--append_dst|--normal_dst) [--OPTIONS]`
#### option
+ --window
+ --windowX 100
+ --windowY 100
+ --sigmaX 1000
+ --sigmaY 1000
### Erosion
`./Erosion.py 'source_path' (--append_dst|--normal_dst) [--OPTIONS]`
#### option
+ --kernel
+ --kernelX 5
+ --kernelY 5
## Rotation
`./Rotation.py 'source_path' angle<int> (--append_dst|--normal_dst)`

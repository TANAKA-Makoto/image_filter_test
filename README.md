# image_filter_test
## dependence
opencv-python
## useage
require either `--append_dst` or `--normal_dst`.  
`--append_dst` is folder path.  
`--normal_dst` is folder path and file name.
### Gaussian
`./Gaussian.py 'source_path' window sigma (--append_dst|--normal_dst) [--OPTIONS]`
#### option
+ --windowX <int>
+ --windowY <int>
+ --sigmaX <int>
+ --sigmaY <int>
### Erosion
`./Erosion.py 'source_path' kernel (--append_dst|--normal_dst) [--OPTIONS]`
#### option
+ --kernelX <int>
+ --kernelY <int>
### Erosion
`./Dilation.py 'source_path' kernel (--append_dst|--normal_dst) [--OPTIONS]`
#### option
+ --kernelX <int>
+ --kernelY <int>
## Rotation
`./Rotation.py 'source_path' angle<double> (--append_dst|--normal_dst)`

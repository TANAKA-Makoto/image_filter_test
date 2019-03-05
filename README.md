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
+ --window <int>
+ --windowX <int>
+ --windowY <int>
+ --sigmaX <int>
+ --sigmaY <int>
### Erosion
`./Erosion.py 'source_path' (--append_dst|--normal_dst) [--OPTIONS]`
#### option
+ --kernel <int>
+ --kernelX <int>
+ --kernelY <int>
## Rotation
`./Rotation.py 'source_path' angle<int> (--append_dst|--normal_dst)`

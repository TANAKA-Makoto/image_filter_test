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
### Rotation
`./Rotation.py 'source_path' angle<double> (--append_dst|--normal_dst)`

## Tips
### Filter and Parameters append name
using `--append_dst` , the value behavior like prefix. and script append there filter name and parameters after source file name.
```
# ./Erosion.py '~/img/test.png' 3 --append_dst '~/img/'
~/img/test-E(3,3).png
```
### pipe line with standard I/O
useing `--cmd`, script standard output becomes only output file name.
so you can use pipe line.
```
# ./Erosion.py '~/img/test.png' 3 --append_dst '~/img/' --cmd | ./Dilation.py 3 --append_dst '~/img/' --cmd 
~/img/test-E(3,3)-D(3,3).png
```

# knn_simple_verify_code
基于knn的简易验证码识别。
## 使用方法：
先使用img_code_dataset.py文件创建训练集；
然后使用knn_train.py进行训练；
然后用knn_accuracy_rate.py检查验证识别率；
verify.py：基于训练好的模型进行验证，使用方法；
```
python3 verify 验证码图片路径
```
验证：
！[test](https://github.com/VVzv/knn_simple_verify_code/blob/master/test.jpg)

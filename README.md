# knn_simple_verify_code
基于knn的简易验证码识别，模型比较单一，识别其余验证码需要单独训练。
### 环境：
python3
依赖库：
```
pip install -r requirements.txt
```
## 使用方法：
先使用img_code_dataset.py文件创建训练集；
然后使用knn_train.py进行训练；
训练好的模型将会保存在models文件夹中；
然后用knn_accuracy_rate_old.py或者knn_accuracy_rate.py检查验证识别率；
verify.py：基于训练好的模型进行验证，使用方法；
##### 使用knn_accuracy_rate.py需要把test_data的图片换个位置，然后在用img_code_dataset.py对测试的图片进行切割；
```
python3 verify.py 验证码图片路径
```
验证：
![test](https://github.com/VVzv/knn_simple_verify_code/blob/master/test.jpg)

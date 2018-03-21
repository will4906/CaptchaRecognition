# Sipo3

关于最最简单的计算题验证码，还是接着之前的思路。灰度图-> 二值化 -> 切割 -> knn

环境依赖

```python
numpy, pillow, sklearn
```

### 灰度图、二值化

```python
image = np.asarray(Image.open(os.path.join('label', file)).convert('L'))
image = (image > 135) * 255
```

### 切割

```python
letters = [image[:, 6:18].reshape(20*12), image[:, 19:31].reshape(20*12), image[:, 33:45].reshape(20*12), image[:, 45:57].reshape(20*12)]
```

### 训练

```python
knn = KNeighborsClassifier()
knn.fit(np.asarray(train_x), np.asarray(train_y))
```

### 总结

太过简单，不在赘述
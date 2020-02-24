# pyplot-cheatsheet

## Hint
Matplotlib doesn't work with pixels directly, but rather physical sizes and DPI. If you want to display a figure with a certain pixel size, you need to [know the DPI of your monitor](https://www.infobyip.com/detectmonitordpi.php).

Here's how to show an 800x800 pixel image in my monitor (`my_dpi=96`):
```python
plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)
```

## Use it with jupyter notebook
### install
```
pip3 install jupyter
pip3 install ipython
```

### run 
```
jupyter notebook
```

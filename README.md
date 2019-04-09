# Attention_visualizer
A simple visualization of attention weights on text for notebook using d3. 

## Usage
The function requires sentence tokens as list with corresponding attention weights as another list.
```
sentence = [ 'i', 'liked', 'the', 'movie', 'it', 'was', 'entertaining']
attention_weights = [1.5457647e-02, 6.5744676e-02, 1.8066147e-04, 1.2420971e-02, 1.6833000e-03, 4.1709002e-04, 4.4919562e-01]
 
display_attention(sentence,attention_weights)
```
![attention_img](https://github.com/shashwattrivedi/Attention_visualizer/blob/master/images/attention_1.PNG)

You can hover over the word to get the attention weight value.

![attention_hover_img](https://github.com/shashwattrivedi/Attention_visualizer/blob/master/images/attention_2.png)

Another style
```
display_attention(sentence,attention_weights,
                  scale=40,  #max increase in font-size
                  offset=18, #base font-size for whole text
                  style=0)   #for 2nd style
```
![attention_style2](https://github.com/shashwattrivedi/Attention_visualizer/blob/master/images/attention_style2.png)

from IPython.core.display import display, HTML
from string import Template
import json

html_template = Template('''<script src="https://d3js.org/d3.v4.min.js"></script>

<style>$css_text</style>
<script>$js_text</script>
<div id = 'text'></div>''')

css_text = '''html, body {
    margin: 0;
    padding: 0;
}
'''

js_template = Template('''
var dataset =[["This",0.4],["is",0.3],["a",0.2],["text",0.4]]
var seconddataset = ["Hello","World"]

function float2int (value) {
    return value | 0;
}

function tohex(fraction)
{
  var value = float2int(256 * fraction);
  var mapping = ['A','B','C','D','E','F'];
  var hex="";
  
  while(value!==0)
    {
      var curr= value%16;
      if(curr >9)
        {
          hex = mapping[curr-10] + hex;
        }
      else
        hex = curr + hex;
      value = float2int(value/16);
    }

  return hex;
}

// Create Event Handlers for mouse
function handleMouseOver(d, i) {  // Add interactivity

      // Use D3 to select element, change color and size
      d3.select(this).attr({
        fill: "orange"
      });

      // Specify where to put label of text
      svg.append("text").attr({
         id: "t" + d.x + "-" + d.y + "-" + i,  // Create an id for text so we can select it later for removing on mouseout
          x: function() { return xScale(d.x) - 30; },
          y: function() { return yScale(d.y) - 15; }
      })
      .text(function() {
        return [d.x, d.y];  // Value of the text
      });
    }


d3.select('#text')
.selectAll('#text')
.data($data)
.enter()
.append('tspan')
.style('font-family','verdana')
$style
.style('margin','2px')
.style('font-size',function(d){return  $offset +$scale*d.weight + "px" ;})
.text(function(d){
  return d.token+" " ;
});



''')

style1 =".style('background-color', function(d,i){return '#FF' +tohex(1-d.weight) +tohex(1-d.weight) ;})"

def display_attention(sentence,attention_weights,scale,offset,style=1):
  data = [{'token':token, 'weight' :weight} for token,weight in zip(sentence,attention_weights)]
  
  if style ==1 :
    js_text = js_template.substitute({'data' : json.dumps(data),'scale': 0, 'offset':20, 'style': style1})
  else:
    js_text = js_template.substitute({'data' : json.dumps(data),'scale': scale, 'offset':offset, 'style': ""})
    
  return display(HTML(html_template.substitute({'css_text':css_text,'js_text':js_text})))
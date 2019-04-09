from IPython.core.display import display, HTML
from string import Template
import json

def display_attention(sentence,attention_weights,scale=0,offset=18,style=1):
  
  if( len(sentence)!=len(attention_weights)):
		raise Exception("Number of tokens "+ len(sentence) + " not equal to \
			attention list length " + len(attention_weights))

	for _ in attention_weights:
		if _ >1.0 or _ < 0.0:
			raise Exception("invalid value " + str(_) + "in attention_weights")
  
  html_template = Template('''
  <script src="https://d3js.org/d3.v4.min.js"></script>
  <style>$css_text</style>
  <script>$js_text</script>
  <div id = 'text' style="margin-left:50px;"></div>
  ''')

  css_text = '''
  html, body {
      margin: 0;
      padding: 0;
  }

  .tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black;
  }
  .tooltip:hover .tooltiptext {
    visibility: visible;
  }

  .tooltip .tooltiptext {
    visibility: hidden;
    font-size:15px;
    width: 60px;
    background-color: black;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 1px 0;
    position: absolute;

    left: 50%;
    margin-left: -60px;
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
    var value = float2int(255 * fraction);
    if(value==0)
      return "00"
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

  d3.select('#text')
  .selectAll('#text')
  .data($data)
  .enter()
  .append('tspan')
  .style('font-family','verdana')
  $style
  .style('margin','2px')
  .attr("class","tooltip")
  .style('font-size',function(d){return  $offset +$scale*d.weight + "px" ;})
  .attr("onmouseover", "handleMouseOver()")
  .text(function(d){
    return d.token+" " ;
  })
  .append('span')
  .attr('class',"tooltiptext")
  .text(function(d){
  return Math.round(d.weight*10000)/100;
  });
  ''')

  style1 =".style('background-color', function(d,i){return '#FF' +tohex(1-d.weight) +tohex(1-d.weight) ;})"  
  data = [{'token':token, 'weight' :weight} for token,weight in zip(sentence,attention_weights)]

  js_text = js_template.substitute({'data' : json.dumps(data),'scale': 0 if style==1 else scale, 'offset':offset, 'style': style1 if style==1 else ""})

    
  return display(HTML(html_template.substitute({'css_text':css_text,'js_text':js_text})))

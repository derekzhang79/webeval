SyntaxHighlighter.brushes.Xml=function(){function a(e,i){var f=SyntaxHighlighter.Match,h=e[0],c=new XRegExp("(&lt;|<)[\\s\\/\\?]*(?<name>[:\\w-\\.]+)","xg").exec(h),b=[];if(e.attributes!=null){var d,g=new XRegExp("(?<name> [\\w:\\-\\.]+)\\s*=\\s*(?<value> \".*?\"|'.*?'|\\w+)","xg");while((d=g.exec(h))!=null){b.push(new f(d.name,e.index+d.index,"color1"));b.push(new f(d.value,e.index+d.index+d[0].indexOf(d.value),"string"))}}if(c!=null){b.push(new f(c.name,e.index+c[0].indexOf(c.name),"keyword"))}return b}this.regexList=[{regex:new XRegExp("(\\&lt;|<)\\!\\[[\\w\\s]*?\\[(.|\\s)*?\\]\\](\\&gt;|>)","gm"),css:"color2"},{regex:new XRegExp("(\\&lt;|<)!--\\s*.*?\\s*--(\\&gt;|>)","gm"),css:"comments"},{regex:new XRegExp("(&lt;|<)[\\s\\/\\?]*(\\w+)(?<attributes>.*?)[\\s\\/\\?]*(&gt;|>)","sg"),func:a}]};SyntaxHighlighter.brushes.Xml.prototype=new SyntaxHighlighter.Highlighter();SyntaxHighlighter.brushes.Xml.aliases=["xml","xhtml","xslt","html","xhtml"];
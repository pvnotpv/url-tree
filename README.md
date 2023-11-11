# url-tree  
### Useful to map a site especially when bughunting.
<p float="left">
  <img src="https://github.com/pvnotpv/url-tree/blob/main/images/img.png?raw=true" width="440" />
</p>

The bash script is used to beautify the output
```
sed -e '$s/├/└/' -e '3s/├/┌/' | sed -e 's/^/      /' | sed -e '1,2d'
```
- If these special characters aren't supported replace them with a dash.
- The node.nodeid property can be used to print the node number of each items, used to change the color of nodes.
### Todo
- Implement a better version in golang.

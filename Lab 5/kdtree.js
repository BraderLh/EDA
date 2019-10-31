k=2;

class Node{
	constructor(point, axis){
		this.point = point;
		this.left = null;
		this.right = null;
		this.axis = axis;
	}
}

function isEmpty()
{
	return this.points.length==0;
}

function getHeight(node) {
	if(node==null)
	{
		return 0;
	}
	else{

		return Math.max(getHeight(node.left),getHeight(node.right))+1;	
	}

}
function generate_dot(node) {
	
	if(node==null)
	{
		return;
	}
  	if(node.left){
    	console.log('"'+node.point+'"'+"->"+'"'+node.left.point+'"');
    	generate_dot(node.left);
  	}
  	if(node.right){
    	console.log('"'+node.point+'"'+"->"+'"'+node.right.point+'"');
    	generate_dot(node.right);
  	}
}
function build_kdtree(points, depth = 0) {
	var n=points.length;
	this.axis = depth%k;

	if(n<=0){
		return null;
	}
	if(n==1){
		return new Node(points[0],axis);
	}
	var median = Math.floor(points.length/2);
	points.sort(function(a,b){return a[axis]-b[axis]});
	
	var left = points.slice(0,median);
	var right= points.slice(median+1);
	var node = new Node(points[median].slice(0,k),axis);
	
	node.left = build_kdtree(left,depth+1);
	node.right = build_kdtree(right,depth+1);
	return node;
}

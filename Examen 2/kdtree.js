k=2;
number = 1;
height_left=0;
height_right = 0;
space_between_nodes = 60;
class Node{
	constructor(point,axis,x,y){
		this.point = point;
		this.left = null;
		this.right = null;
		this.axis = axis;
		this.x = x;
		this.y = y;
	}
	esHoja(){
		return(!this.left);
	}

	visit(parent, number = 1) {
		if(this.point==null)
		{
			return;
		}
		if(this.left!=null){
			fill(255);
			this.left.visit(this, number + 1);
		}
		console.log("Curr point: ",this.point);
		// fill(255);
		// noStroke();
		// text('['+this.point+']',this.x,this.y);
		// stroke(255);
		// fill(1,0);
		// ellipse(10*number, this.y, 100, 40);
		// this.x = number*10;
		this.number = number;

		if(this.right!=null){
			this.right.visit(this, number + 1);
		}
	}

	inorder_traversal(){
		if (this.left != null){
			var p_x = this.left.point[0];
			var part_y = this.left.point[1];
			console.log(part_y);
			stroke(41, 128, 185 );
	   		line(51,398-part_y,p_x,398-part_y);
			this.left.inorder_traversal();
		}
		this.number = number;
		this.x = number*space_between_nodes;
		number += 1;
		console.log(this.point);
		if (this.right != null){
			var part_x = this.right.point[0];
			var part_y = this.right.point[1];
			stroke(192,57,43);
	   		line(part_x,0,part_x,349);
			this.right.inorder_traversal();
		}
	}
	postorder_traversal() {
		if(this.left!=null){
			var part_x = this.left.point[0];
			var part_y = this.left.point[1];
			stroke(41, 128, 185 );
	   		line(51,398-part_y,part_x,398-part_y);
			
			this.left.postorder_traversal();
		}
		if(this.right!=null){
			var part_x = this.right.point[0];
			var part_y = this.right.point[1];
			stroke(41, 128, 185 );
	   		line(51,398-part_y,part_x,398-part_y);
			
			this.right.postorder_traversal();
		}
		this.number = number;
		this.x = number*space_between_nodes;
		number += 1;
		console.log(this.point); 
	}
	visit2(){
		fill(255);
		noStroke();
		text('['+this.point+']',this.x,this.y);
		stroke(255);
		fill(1,0);
		ellipse(this.x, this.y, 100, 40);
		if (this.left != null){
			this.left.visit2();
		}
		if (this.right != null){
			this.right.visit2();
		}
		
	}
	generate_dot() {
		if(this.point==null)
		{
			return;
		}
	  	if(this.left!=null)
	  	{
			console.log('"'+this.point+'"'+"->"+'"'+this.left.point+'"');
			console.log("Debug: ",this.x,this.y+20, this.left.x, this.left.y-20)
			stroke(255);
			line(this.x,this.y+20, this.left.x, this.left.y-20);
	    	this.left.generate_dot();
	  	}
	  	if(this.right!=null){
			console.log('"'+this.point+'"'+"->"+'"'+this.right.point+'"');
			line(this.x,this.y+20, this.right.x, this.right.y-20);			
	    	this.right.generate_dot();
		}
		fill(255);
		noStroke();
		text('['+this.point+']',this.x,this.y);
		stroke(255);
		fill(1,0);
		ellipse(this.x, this.y, 100, 40);
		
	}
	getHeight() {
		if(this.point == null){
			return 0;
		}
		else if(this.left!=null){
			height_left ++;
			this.left.getHeight();
		}
		else if(this.right!=null){
			height_right++;
			this.right.getHeight();
		}
		return Math.max(height_left,height_right);
	}
}


class KdTree {
	constructor(points){
		this.root = null;
		this.count=0;
	}
	build(points){
		var initial_x = width/2;
		var initial_y = 40;
		this.root = this.build_kdtree(points, initial_x, initial_y);
		
		var part_x = this.root.point[0];
		stroke(255, 255, 0);
	    line(part_x,0,part_x,349);
	}
	build_kdtree(points, x, y, depth=0) {
		var n=points.length;
		var axis = depth%k;
		if(n<=0){
			return null;
		}
		if(n==1){
			return new Node(points[0],axis,x, y);
		}

		var median = Math.floor(points.length/2);

		points.sort(function(a,b){return a[axis]-b[axis]});
		
		var left = points.slice(0,median);
		var right= points.slice(median+1);
		
		this.count++;
		
		var node = new Node(points[median].slice(0,k),axis, x, y);

		
		node.left = this.build_kdtree(left,x-50, y+70,depth+1);
		node.right = this.build_kdtree(right,x+50, y+70,depth+1);
		return node;
	}
	visualize() {
		this.root.generate_dot();
	}
	traverse(){
		// var number = 1;
		// this.root.visit(this.root, number);
		console.log('Recorrido InOrder: ');
		this.root.inorder_traversal();
	}
	traverse2(){
		console.log('Recorrido PostOrder: ');
		this.root.postorder_traversal();
	}
	height(){
		console.log('Altura:  '+this.root.getHeight());
	}
}
var kdt;

function setup() {
	var width = 450;
	var height = 400;
	createCanvas(width,height);
	background(213, 219, 219);
	//stroke(255);
	
	line(1,height-51,width,height-51);
	
	line(49,height-1,49,1);
	
	line(width-1,height-51,435,340);
	line(width-1,height-51,435,360);

	line(49,0,60,15);
	line(49,0,40,15);

 	var data = [];
	for(let i = 0; i < 6; i++){
	       var x = Math.floor(Math.random() * (350-51)+50);
	       var y = Math.floor(Math.random() * (400-101)+59);
	       data.push([x, y]);	       
	       fill(1);
	       circle(x, height - y, 10); //200-y para q se dibuje apropiadamente
	       
	       //eje y: 
	       //stroke(41, 128, 185 );
	       //line(51,400-y,x,400-y);
	       
	       //eje x:
	       //stroke(192,57,43);
	       //line(x,0,x,height-y);

	       textSize(10);
	       stroke(255);
	       text('['+x + ',' + y+']', x + 5, height - y);

	}
	kdt = new KdTree(); 
	kdt.build(data);
	kdt.traverse();
	kdt.traverse2();
	console.log(kdt);
	console.log('Formato Dot y Posiciones de los Nodos: ')
	//kdt.visualize();
	kdt.height();

}
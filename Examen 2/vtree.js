var kdt;
function setup() {
	createCanvas(900,500);
	background(51);
	noSmooth();
	//stroke(255);
	ellipseMode(CENTER);
	textAlign(CENTER, CENTER);
 	var data = [];
	for(let i = 0; i < 13; i++){
	       var x = Math.floor(Math.random() * (350-51)+50);
	       var y = Math.floor(Math.random() * (400-101)+59);
	       data.push([x, y]);

	}
	kdt = new KdTree(); 
	kdt.build(data);
	kdt.traverse();
	console.log(kdt);
	console.log('Formato Dot y Posiciones de los Nodos: ')
	kdt.visualize();
	kdt.height();
}


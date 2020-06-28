const {
  performance
} = require('perf_hooks');
const before3 = performance.now();

var count1=0;

var nbMessageSent = 1000;
var mqtt = require('mqtt');
var client = mqtt.connect("mqtt://test.mosquitto.org", {clientId:"mqttjs01"});
var message="Avantages Azure IoT Les clients existants soulignent divers avantages de Microsoft Azure en fonction des spécificités de leur secteur Simplicité. Microsoft a vraiment investi pour rendre sa plateforme IoT pratique et simple pour différents utilisateurs, quelles que soient leurs compétences. De la connexion dTarification flexible. Chaque service Azure IoT a son propre modèle de tarification, en fonction de ses spécificités et de ses fonctionnalités. Ce qui distingue vraiment la tarification Azure IoT, capproche simple et la transparence. Par exemple, le coût du combo Amazon Sphere (puce, système dutilisation populaires dans Azure IoT Central. Ou se compose entièrement dAccuweather. Le service Azure Digital Twins  permet de créer une représentation virtuelle de l’environnement IoT physique et de déterminer les dépendances, corrélations et relations entre ses parties. Une sécurité renforcée. LAzure IoT estRéseau de partenaires puissant. Tout comme AWS, Azure a une l";
//message= message+message; // 2 Ko
//message= message+message+message+message; // 4 kO
//message= message+message+message+message+message+message+message+message; // 8 ko
message= message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message;//48 k
console.log("The size of message is : " + message.length + " characters, " + Buffer.byteLength(message, 'utf8') + " bytes");
console.log(" The nomber of messages is : " + nbMessageSent);
client.on("connect",function(){	
console.log("connected  "+ client.connected);

});

client.on('message', function (topic, message) {
console.log(message.toString());
});
client.on('offline', function() {
    console.log("offline");
});

const before1 = performance.now();

var temp =0;
while (count1 <1) {
	
	for (let pas = 1; pas <= nbMessageSent; pas++) {
        	console.log( "Message number : " + pas +" from client A");
                const before2 = performance.now();
		client.publish('presence12', message);
                const after2 = performance.now();
                duration3 =after2 - before2;
                temp= temp+ duration3;
	}

        count1= count1 +1;
//}
	const after1 = performance.now();


	console.log("the average time to send a single message is :"+(temp/nbMessageSent)/1000 + " Seconds ");
	console.log("the net time to send " + nbMessageSent +" messages is : " +temp/1000 + " Seconds ");
	console.log("time left in the loop to send " + nbMessageSent + " messages is : " + (after1 - before1)/1000+ " Seconds");
}

var timer_id=setInterval(function(){},0000);
const after3 = performance.now();
//console.log("Program execution time is : "+(after3-before3)/1000 + " Seconds ");  







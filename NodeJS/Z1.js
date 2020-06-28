var settings = {
keepalive: 1000,
clientId: 'RANDOM_CLIENT_STRiNG_hERE',
username: 'YOUR_BROKER_USERNAME',
password: 'YOUR_BROKER_PASSWORD',
port: 1883
}

var mqtt = require('mqtt');
var client = mqtt.connect("mqtt://test.mosquitto.org", {clientId:"mqttjs02"});

client.on('connect', function () {
client.subscribe('presence12');

});

client.on('message', function (topic, message) {

console.log("Message recieved " +message.toString());
console.log("The size of message is : " + message.length + " characters, " + Buffer.byteLength(message, 'utf8') + " bytes");

});

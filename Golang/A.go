package main

import (
    "fmt"
    MQTT "github.com/eclipse/paho.mqtt.golang"
    "os"
    "os/signal"
    "syscall"
    "time"
    
)
var start = time.Now()
var knt int
var f MQTT.MessageHandler = func(client MQTT.Client, msg MQTT.Message) {
   // fmt.Printf("MSG: %s\n", msg.Payload())
    //text := fmt.Sprintf("this is result msg #%d!", knt)
    //knt++
    //token := client.Publish("TestTopic", 0, false, text)
    //token.Wait()
    //fmt.Sprintf("this is result msg #%d!", knt)
    //knt++
    // fmt.Printf("MSG: %d", msg.Payload())
    //fmt.Printf("this is result msg #%d!")
}
/*
func MultiplyDuration(factor float64, d time.Duration) time.Duration {
    return time.Duration(factor) * d        // method 1 -- multiply in 'Duration'
 // return time.Duration(factor * int64(d)) // method 2 -- multiply in 'int64'
}*/
func main() {
    knt = 0
    c := make(chan os.Signal, 1)
    signal.Notify(c, os.Interrupt, syscall.SIGTERM)

    opts := MQTT.NewClientOptions().AddBroker("test.mosquitto.org:1883")
    opts.SetClientID("mac-go1")
    opts.SetDefaultPublishHandler(f)
    topic := "TestTopic"

    opts.OnConnect = func(c MQTT.Client) {
            if token := c.Subscribe(topic, 0, f); token.Wait() && token.Error() != nil {
                    panic(token.Error())
            }
    }
    client := MQTT.NewClient(opts)
    if token := client.Connect(); token.Wait() && token.Error() != nil {
            panic(token.Error())
    } else {
            fmt.Printf("Connected to server\n")
    }
    var msgNum int = 1000
    fmt.Println("The number of messages is : ",msgNum )
     
    message := "Avantages Azure IoT Les clients existants soulignent divers avantages de Microsoft Azure en fonction des spécificités de leur secteur Simplicité. Microsoft a vraiment investi pour rendre sa plateforme IoT pratique et simple pour différents utilisateurs, quelles que soient leurs compétences. De la connexion dTarification flexible. Chaque service Azure IoT a son propre modèle de tarification, en fonction de ses spécificités et de ses fonctionnalités. Ce qui distingue vraiment la tarification Azure IoT, capproche simple et la transparence. Par exemple, le coût du combo Amazon Sphere (puce, système dutilisation populaires dans Azure IoT Central. Ou se compose entièrement dAccuweather. Le service Azure Digital Twins  permet de créer une représentation virtuelle de l’environnement IoT physique et de déterminer les dépendances, corrélations et relations entre ses parties. Une sécurité renforcée. LAzure IoT estRéseau de partenaires puissant. Tout comme AWS, Azure a une l"  
    //message= message+message; // 2 Ko
    //message= message+message+message+message; // 4 kO
    //message= message+message+message+message+message+message+message+message; // 8 ko
    message= message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message+message;//48 k
    //var fr = time.Nanosecond
    //var temp_oneMessage = time.Nanosecond
    //var t = 0.1
    var temp = time.Nanosecond
   
    var length = len(message)
    fmt.Printf("The Size of message is : ")
    fmt.Println(length, " bytes") 
    start2 := time.Now()
    for i := 0; i < msgNum; i++ {

        fmt.Print("message published number ", i+1, "\n")
        start1 := time.Now()
       
        //token := client.Publish(topic, 0, false, message)
        client.Publish(topic, 0, false, message)
        end1 := time.Now()
        elapsed := end1.Sub(start1)
        temp = temp+ elapsed
        //temp_oneMessage =elapsed
      
        /*if token.Error() != nil {
            fmt.Printf("Failed to publish, err: %v\n", token.Error())
            os.Exit(1)
        }*/
    
    }
    end2 := time.Now()
    elapsed1 := end2.Sub(start2)
    //fmt.Print("the average time to send a single message is :", time.Duration(temp*(t))* time.Millisecond , " Seconds\n ") 
    //fr = MultiplyDuration(t, temp)
    //fmt.Print("the average time to send a single message is :", fr, " Seconds\n ") 
    //fmt.Print("The  time to send a single message is :", temp_oneMessage , " \n") 
    fmt.Println("The net time to send " , msgNum, " messages is : ", temp) 
    fmt.Println("Time left in the loop to send ", msgNum, " messages is : ", elapsed1)  

    fmt.Print("Disconnect Client After publishing ", msgNum, " Messages\n")
    client.Disconnect(250)
    
    
     
    
elapsed := time.Since(start)
fmt.Printf("Program execution time is %s", elapsed)   
fmt.Printf("\n")
}

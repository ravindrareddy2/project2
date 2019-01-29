document.addEventListener("DOMContentLoaded",()=>{

    //connect to web socket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    //on connected to web socket
    socket.on("connect",() => {

        //button to emit submit channel
        document.querySelector("button").onclick = () =>{
            const selection = document.getElementById("#newchannel").value;
            socket.emit("submit channel", {"selection": selection})

        }


    })

    //on submiting channel
    socket.on("announce channel", data => {
        const li = document.createElement("li");

        li.innerHTML = `<a href="/chatroom/${data["chatlist"]}"> ${data["selection"]} </a>`;
        console.log(li.innerHTML);
        document.querySelector("#chatlist").append(li);

    })

})
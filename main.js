const mineflayer = require("mineflayer")


const chater = mineflayer.createBot(
    {
        host: "mc.icraft.cc",
        username: "_chater",
        port: 49282, 
        version: "1.16.5",
    }
)


function chat_to_game(msg)
{
    chater.once('spawn', () => { chater.chat(msg) })
}


chater.on('chat', (username, message) => {
    if(username == chater.username) return;
    if(message == '1')  chater.chat("/tpaccept")
})

chater.on('message', (message) => {
    console.log(message.toAnsi())
})

// chater.on("login", (login) =>{
//     chat_to_game("/l tt5566tt")
// })
chat_to_game("/l tt5566tt")
chat_to_game("有人吗？wanghany马上来")
chat_to_game("/tpa wanghany")
chat_to_game("/tpa wanghany")


const mineflayer = require("mineflayer")


const chater = mineflayer.createBot(
    {
        host: "mc.icraft.cc",
        username: "wanghany",
        port: 49282, 
        version: "1.16.5",
    }
)

function chat_to_game(msg)
{
    chater.once('spawn', () => { chater.chat(msg) })
}


chater.on('message', (message) => {
    console.log(message.toAnsi())
})

chater.on("login", (login) =>{
    chat_to_game("/l tt5566tt")
})


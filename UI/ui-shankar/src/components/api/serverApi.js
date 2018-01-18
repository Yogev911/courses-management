
import jsonp from 'jsonp'
import jsonpP from 'jsonp-p'
//http://localhost:3000/API/data/dept_info.json?callback=__jp0
const myPromise = (url,obj) => {
    console.log("TEST 2")
    return new Promise((resolve,rej) => {
        jsonp(url,obj,null,(err,res)=>{
            if(err) {
                rej(err)
                console.log("ERR",err)
            }
            resolve(res)
        })
    })
    
}
class ServerApi{
    getAllJson(){
        
        return new Promise((resolve,reject)=>{
            const url = 'https://new-nerves.herokuapp.com/getAllSongs'
            
            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    const jsObj = JSON.parse(this.responseText);
                    console.log(jsObj)
                    resolve(jsObj);
                }
            };
            xmlhttp.open("GET", 'https://yogev-test1.herokuapp.com/getjson', true);
            xmlhttp.send();

        })
       
    }
}

let serverapi = new ServerApi()
export { serverapi };
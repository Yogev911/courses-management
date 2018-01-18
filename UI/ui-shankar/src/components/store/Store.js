import {observable} from 'mobx'
import React from 'react'
import {serverapi} from '../api/serverApi'


let momentDay = null

const Store = observable({
    get momentDay(){
        return momentDay;
    },
    setMoment(time){
        switch(time === Number && time){
            case time > 20 : momentDay = "Night"
                             break;
            case time > 18 : momentDay = "Evening"
                             break;
            case time > 15 : momentDay = "Afternoon"
                             break;
            case time > 12 : momentDay = "Noon"
                             break;
            case time > 3  : momentDay = "Morning"
                             break;
            default : "Nighttt"
        }
    }

})
 
const ApiStore = () => {
    const store = observable({
        fun : serverapi.getAllJson().then(res => store.data = res),
        data : null,
        get getData(){
            console.log(store.data)
            return store.data ? store.data : null;
        }
    })

    return store;
}


export  {Store , ApiStore} ;
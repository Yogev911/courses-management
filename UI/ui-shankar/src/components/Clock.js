import React from 'react'
import {Store} from './store/Store'
import { Observer } from 'mobx-react'

const days = ["Sun","Mon","Tues","Thurs","Wed","Fri","Sat"]
const moment = require('moment')
const date = new Date();

class Seconds extends React.Component{
    state = { sec : this.props.seconds }
    render(){
        let {sec} = this.state
        let secApper = sec%60
        setTimeout(()=> this.setState({ sec : sec+1 }),1000)
        return(
            <span>{secApper<10 && "0"}{secApper}</span>
        )
    }
}

class Minutes extends React.Component{
    state = { min : this.props.minutes , defaultTimeout : this.props.timeout }
    render(){
        let {min , defaultTimeout} = this.state

        let minApper = min%60
        setTimeout(()=> this.setState({ min : minApper+1  , defaultTimeout : 60000}),Number(defaultTimeout))
        return(
            <span>{minApper < 10 &&"0"}{minApper}</span>
        )
    }
}


class Hours extends React.Component{
    state = { hour : this.props.hour  , defaultTimeout : this.props.timeout}
    render(){
        let {hour , defaultTimeout} = this.state
        setTimeout(()=> this.setState({ hour : date.getHours()  , defaultTimeout : 600000}),Number(defaultTimeout))
        return(
            <span>{hour}</span>
        )
    }

}

// const obsrvDay = Observer(({store : {stroeMoment}}) =>{
//     return <div>{stroeMoment}</div>
// })
const myTime = () =>{
    return moment().format('MMMM Do YYYY, h:mm:ss  a')
}

class Moment extends React.Component{
    state = {time : myTime()}
    render(){
        let { time } = this.state
        setTimeout(()=> this.setState({time : myTime()}) , 1000)

        return(
            <span>{time}</span>
        )
    }
}
const Clock = () => (
    <h3 style={{fontFamily:"fantasy"}}>
    {/* {moment().format('MMMM Do YYYY, h:mm:ss a')}<br/> */}
    <div><Moment/></div>
        {/* <table>
            <tbody>
                <tr>
                    <td>{days[date.getDay()]} - </td>
                    <td><Hours hour={date.getHours()} timeout={600000 - date.getMinutes()*1000}/></td>
                    <td>:</td>
                    <td><Minutes minutes={date.getMinutes()} timeout={60000-date.getSeconds()*1000}/></td>
                    <td>:</td>
                    <td><Seconds seconds={date.getSeconds()}/></td>
                </tr>
            </tbody>
        </table> */}
    </h3>
)

export default Clock;
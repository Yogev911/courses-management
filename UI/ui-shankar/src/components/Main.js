import React from 'react'
import { ApiStore } from './store/Store'
import {observer} from 'mobx-react'


const colStyle = { width : 100 , textAlign : "center"}

class AllMainData extends React.Component{

    render(){
        return null
    }
}

 const ObjMain = ({data}) =>(
    <div style={{backgroundColor : "#f5f5f5" , width:300}}>
        <h3 style={{backgroundColor:'#B2CBE5' , color:"white" , textAlign:"center" , marginBottom:-2.5 , padding:1}}>Year - {data.year}</h3>
        <table>
            <thead style={{width:300}}>
                <tr>
                    <th style={colStyle}>Number</th>
                    <th style={colStyle}>Name</th>
                    <th style={colStyle}>Points</th>
                </tr>
            </thead>
            <tbody>
                {data.courses.map((obj,i)=>
                    <tr key={i} style={{backgroundColor : i%2 == 0 ? "#c6e2ff" : "white"}}>
                        <td style={colStyle}>{obj.course_number}</td> 
                        <td style={colStyle}>{obj.name}</td> 
                        <td style={colStyle}>{obj.points}</td> 
                    </tr>
                )} 
            </tbody>
        </table>
    </div>
 )

const MainObsrv = observer( ({obsrv}) => {
    console.log("TEST" ,  obsrv.getData)
    return obsrv.getData? obsrv.getData.map((obj,i)=><ObjMain key={i} data={obj} />) : null
})

export const Main = () => (
    <MainObsrv obsrv={ApiStore()}/>
)

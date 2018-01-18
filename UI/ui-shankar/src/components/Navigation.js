import React from 'react'
import { Nav , NavItem , NavLink} from 'reactstrap'
import classnames from 'classnames';
import { BrowserRouter , Switch, Route, Link } from 'react-router-dom';
import Header from './Header'
import {Main} from './Main'

import '../styles/nav.css'


class Tab extends React.Component{
    constructor(props) {
        super(props);
    
        this.toggle = this.toggle.bind(this);
        this.state = {
          activeTab: '1'
        };
      }
    
      toggle(tab) {
        if (this.state.activeTab !== tab) {
          this.setState({
            activeTab: tab
          });
        }
      }
    render(){
        return(
            <div>
                  <Nav tabs style={{marginBottom:25}}>
                    <NavItem>
                        <NavLink
                        tag={Link}
                        className={classnames({ active: this.state.activeTab === '1' })}
                        onClick={() => { this.toggle('1'); }}
                        to={'/'} 
                        style={{ textDecoration:"none"}}>
                            Header
                        </NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink
                        tag={Link}
                        className={classnames({ active: this.state.activeTab === '2' })}
                        onClick={() => { this.toggle('2'); }}
                        to={'/Login'} style={{ textDecoration:"none"}}>
                         Main
                        </NavLink>
                    </NavItem>
                    </Nav>
            </div>
        )
    }
}


export class Navigation extends React.Component{
    
    render(){
        return(
            <BrowserRouter>
                <div>
                    <Tab/>
                    
                    <Switch>
                        <Route exact path='/' component={Header} />
                        <Route exact path='/Login' component={Main} />
                    </Switch>
                </div>
            </BrowserRouter>
        )
    }
}
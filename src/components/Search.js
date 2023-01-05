import React, { useEffect, useState } from 'react'
import Appdata from './AppData'
import "./style.css"
import Form from 'react-bootstrap/Form'
import Cards from './Cards'
import gplayLogo from './logo.png' 

const Search = () => {

    const [copydata, setCopydata] = useState([{}]);

    useEffect(()=>{
        fetch('/fetch').then(
            response => response.json()
        ).then(data => setCopydata(data.appname))
    },[]);

    const listItems = copydata.map((copydata)=>{   
        return <li>{copydata}</li>;   
    });   

    return (
        <>
            <ul>{listItems}</ul>
            {/*<section className='iteam_section mt-4 container'>
                <div className="row mt-2 d-flex justify-content-around align-items-center">
                    <Cards data={copydata} />
                </div>
            </section>*/}
            
        </>
    )
}

export default Search
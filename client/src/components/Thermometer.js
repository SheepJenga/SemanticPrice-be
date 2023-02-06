import React, { useEffect, useState } from 'react'
// import Thermometer from 'react-thermometer-component'
import GaugeChart from 'react-gauge-chart'
import ModalContents from './modal-contents'

function MyThermometer(props) {
    const [data, setData] = useState([{}])
    const [open, setOpen] = useState(false)

    let handleOpen = () => {if (!open) {setOpen(true)}}
    let handleClose = () => setOpen(false)

    useEffect(() => {
        fetch(`/api/${props.date}/scores/${props.symbol}/${props.source}`).then(
          res => res.json()
        ).then(
          data => {
            setData(data)
            console.log(data)
          }
        )
      }, [])

    return (
        <div onClick={handleOpen}>
          {/* <Thermometer theme="dark" value="70" max="100" size="large" height="200" /> */}
          <GaugeChart id="gauge-chart3"
            animate={true}
            nrOfLevels={16} 
            colors={["#FF5F6D", "#FFC371"]} 
            arcWidth={0.35}
            percent={data.score + 0.5} />
          
          <ModalContents 
            open={open}
            onClose={handleClose}
            ticker={props.ticker} />
        </div>
    )
}

export default MyThermometer

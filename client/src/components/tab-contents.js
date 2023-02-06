import React from 'react'
import MyThermometer from './thermometer'


function MyTab(props) {

  let today = new Date().toLocaleDateString('en-CA')

  return (
    <div>
      <div style={{
        position: 'absolute', left: '22%', top: '43%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Tesla" symbol="TSLA" date={today} source={props.source} />
      </div>
      <div style={{
        position: 'absolute', left: '50%', top: '43%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Amazon" symbol="AMZN" date={today} source={props.source} />
      </div>
      <div style={{
        position: 'absolute', left: '78%', top: '43%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Meta" symbol="META" date={today} source={props.source} />
      </div>
      <div style={{
        position: 'absolute', left: '22%', top: '80%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Microsoft" symbol="MSFT" date={today} source={props.source} />
      </div>
      <div style={{
        position: 'absolute', left: '50%', top: '80%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Apple" symbol="AAPL" date={today} source={props.source} />
      </div>
      <div style={{
        position: 'absolute', left: '78%', top: '80%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Google" symbol="GOOGL" date={today} source={props.source} />
      </div>
    </div>
  )
}

export default MyTab
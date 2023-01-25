import React, { Component, useState, useEffect} from 'react'
// import Thermometer from './components/Thermometer'
import MyThermometer from './components/Thermometer'
import { Modal, Button, Box, Typography, Shadows } from '@mui/material'
import './App.css'

function App() {
  const [data, setData] = useState([{}])
  const [open, setOpen] = useState(false)

  let handleOpen = () => setOpen(true)
  let handleClose = () => setOpen(false)

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <html>
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet" />
      </head>
      <div style={{
        position: 'absolute', left: '16%', top: '11.5%',
        transform: 'translate(-50%, -50%)'
        }}>
        <h1>Semantic Price</h1>
      </div>
      <div style={{
        position: 'absolute', left: '20%', top: '40%',
        transform: 'translate(-50%, -50%)'
        }} onClick={handleOpen}
        >
        <MyThermometer ticker="Tesla" />
      </div>
      <div style={{
        position: 'absolute', left: '40%', top: '40%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Amazon" />
      </div>
      <div style={{
        position: 'absolute', left: '60%', top: '40%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Meta" />
      </div>
      <div style={{
        position: 'absolute', left: '80%', top: '40%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Microsoft" />
      </div>
      <div style={{
        position: 'absolute', left: '20%', top: '78%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Apple" />
      </div>
      <div style={{
        position: 'absolute', left: '40%', top: '78%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Google" />
      </div>

    </html>
  )
}

export default App
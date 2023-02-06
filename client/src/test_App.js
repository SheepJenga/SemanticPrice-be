import React, { Component, useState, useEffect} from 'react'
import MyThermometer from './components/thermometer'
import { Modal, Button, Box, Typography, Shadows } from '@mui/material'
import './App.css'

function TestApp() {
  return (
    <html>
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet" />
      </head>
      <div style={{
        position: 'absolute', left: '20%', top: '40%',
        transform: 'translate(-50%, -50%)'
        }}>
        <MyThermometer ticker="Tesla" />
      </div>
    </html>
  )
}

export default TestApp
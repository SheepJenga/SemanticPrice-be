import React, { useState } from 'react'
import { Box, Tab } from '@mui/material'
import MyThermometer from './components/thermometer'
// import { Modal, Button, Box, Typography, Shadows } from '@mui/material'
import { TabContext, TabList, TabPanel } from '@mui/lab'
import MyTab from './components/tab-contents'
import './App.css'


function App() {
  const [tab, setTab] = useState('1')
  const handleTabChange = (event, new_tab) => setTab(new_tab)

  let today = new Date().toLocaleDateString('en-CA')

  // useEffect(() => {
  //   fetch("/api/2023-02-02").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data)
  //     }
  //   )
  // }, [])

  return (
    <html>
      <head>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet" />
      </head>
      <Box style={{
        position: 'absolute', left: '16%', top: '9%',
        transform: 'translate(-50%, -50%)'
        }}>
        <h1>Semantic Price</h1>
      </Box>
      <Box>
        <TabContext value={tab}>
          <Box sx={{
            borderBottom: 1, 
            borderColor: 'divider',
            position: 'absolute', 
            left: '50%', 
            top: '20%',
            transform: 'translate(-50%, -50%)' }}>
            <TabList aria-label='Tabs example' onChange={handleTabChange}>
              <Tab sx={{ color: '#FFFFFF' }} label='All' value='1' />
              <Tab sx={{ color: '#FFFFFF' }} label='Barrons' value='2' />
              <Tab sx={{ color: '#FFFFFF' }} label='Bloomberg' value='3' />
              <Tab sx={{ color: '#FFFFFF' }} label='CBNC' value='4' />
              <Tab sx={{ color: '#FFFFFF' }} label='WSJ' value='5' />
              <Tab sx={{ color: '#FFFFFF' }} label='Yahoo' value='6' />
            </TabList>
          </Box>

          <TabPanel value='1'>
            <MyTab source='ALL' />
          </TabPanel>
          <TabPanel value='2'>
            <MyTab source='barrons' />
          </TabPanel>
          <TabPanel value='3'>
            <MyTab source='bberg' />
          </TabPanel>
          <TabPanel value='4'>
            <MyTab source='CBNC' />
          </TabPanel>
          <TabPanel value='5'>
            <MyTab source='wsj' />
          </TabPanel>
          <TabPanel value='6'>
            <MyTab source='yahoo' />
          </TabPanel>
        </TabContext>
      </Box>
      {/* <MyTab /> */}
    </html>
  )
}

export default App
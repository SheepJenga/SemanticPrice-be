import React, { useState } from 'react'
import Thermometer from 'react-thermometer-component'
import { Modal, Box, Typography } from '@mui/material'

function MyThermometer(props) {
    const [open, setOpen] = useState(false)

    let handleOpen = () => setOpen(true)
    let handleClose = () => setOpen(false)

    return (
        <div onClick={handleOpen}>
            <Thermometer theme="dark" value="70" max="100" size="large" height="200" />
            <Modal
            open={open}
            onClose={handleClose}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
            >
                <Box sx={{
                    bgcolor: '#330631',
                    opacity: '95%',
                    boxShadow: 9,
                    borderRadius: 2,
                    p: 2,
                    height: 700,
                    width: 1000,
                    outline: 0,
                    position: 'absolute', 
                    left: '50%', 
                    top: '50%',
                    transform: 'translate(-50%, -50%)'
                }}>
                    <Typography id="modal-modal-title" variant="h2" component="h1">
                    {props.ticker}
                    </Typography>
                    <hr />
                    <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                    Top headlines:
                    </Typography>
                    <div style={{
                    position: 'absolute', left: '22%', top: '55%',
                    transform: 'translate(-50%, -50%)'
                    }}>
                    <Thermometer theme="dark" value="70" max="100" size="large" height="400" />
                    </div>
                    
                </Box>
            </Modal>
            <p>{props.ticker}</p> 
        </div>
    )
}

export default MyThermometer;

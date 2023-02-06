import { Modal, Box, Typography } from '@mui/material'
import CloseIcon from '@mui/icons-material/Close'
import Thermometer from 'react-thermometer-component'

function ModalContents(props) {
    return (
        <div>
            <Modal 
            open={props.open}
            onClose={props.onClose}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description">

                <Box sx={{
                    bgcolor: '#142433',
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
                <CloseIcon 
                sx={{
                    position: 'absolute', 
                    left: '97%', 
                    top: '4%',
                    transform: 'translate(-50%, -50%)'
                }}
                onClick={props.onClose}/>
                    
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

export default ModalContents
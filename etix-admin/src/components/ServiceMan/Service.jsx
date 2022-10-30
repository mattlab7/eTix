import React from 'react'
import { makeStyles } from '@material-ui/styles';
import { Grid, Box, Typography, TextField, Button, Paper } from '@material-ui/core';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from '@mui/material';

import ArrowBackIosTwoToneIcon from '@mui/icons-material/ArrowBackIosTwoTone';
import ArrowForwardIosRoundedIcon from '@mui/icons-material/ArrowForwardIosRounded';
import SearchRoundedIcon from '@mui/icons-material/SearchRounded';
import PrintRoundedIcon from '@mui/icons-material/PrintRounded';
import VisibilityRoundedIcon from '@mui/icons-material/VisibilityRounded';
import EditRoundedIcon from '@mui/icons-material/EditRounded';
import DeleteRoundedIcon from '@mui/icons-material/DeleteRounded';
import AddCircleRoundedIcon from '@mui/icons-material/AddCircleRounded';

const useStyles = makeStyles((theme) => ({
    whole: {
      backgroundImage: `url("https://cdn.discordapp.com/attachments/885034816087683072/885035160016396329/20140625233054-09abeddb-me.jpg")`,
      backgroundRepeat: "no-repeat",
      backgroundSize: "cover",
      backgroundColor: "rgba(255,255,255,0.5)",
      backgroundBlendMode: "lighten",
      fontFamily: ['rubik', 'sans-serif'].join(',')
    },
    inside: {
      paddingTop: '5%',
      paddingBottom: '5%'
    },
    sect: {
        backgroundColor: 'rgba(31,40,51,0.75)',
        color: 'white'
    },
    articles: {
        width: '350px',
        height: '550px'
    },
    tf: {
        width: '250px'
    }
}));

function createData(tick, serviceID, vendorName, route, datetime, status) {
    return { tick, serviceID, vendorName, route, datetime, status };
}

const rows = [
    createData('', 1, 'Transnasional Sdn Bhd', 'LARKIN SENTRAL, JB - TBS, KL', '1/10/2021 16:20', 'ACTIVE'),
    createData('', 2, 'Transnasional Sdn Bhd', 'TBS, KL - LARKIN SENTRAL, JB', '1/10/2021 16:20', 'ACTIVE'),
    createData('', 3, 'Transnasional Sdn Bhd', 'BUTTERWORTH TERM, PP - PUDU SENTRAL, KL', '1/10/2021 16:20', 'ACTIVE'),
    createData('', 4, 'Transnasional Sdn Bhd', 'PUDU SENTRAL, KL - BUTTERWORTH TERM, PP', '1/10/2021 16:20', 'ACTIVE'),
    createData('', 5, 'myRapid Sdn Bhd', 'PUDU SENTRAL, KL - TERMINAL JALAN TAR, PK', '1/10/2021 16:20', 'ACTIVE'),
    createData('', 6, 'myRapid Sdn Bhd', 'PUDU SENTRAL, KL - TERMINAL JALAN TAR, PK', '1/10/2021 16:20', 'ACTIVE'),
    createData('', 6, 'SBS Transit Sdn Bhd', 'TBS, KL - GOLDEN MILE COMPLEX, SG', '1/10/2021 16:20', 'ACTIVE'),
    createData('', 6, 'SBS Transit Sdn Bhd', 'GOLDEN MILE COMPLEX, SG - TBS, KL', '1/10/2021 16:20', 'ACTIVE'),
  ];

function Service() {
    const classes = useStyles();
    return (
        <Box className={classes.whole}>
            <Grid container direction="column" justifyContent="center" alignItems="center" spacing={4} className={classes.inside}>
                <Grid item>
                    <Grid container direction="row" justifyContent="flex-start" alignItems="center" spacing={4} >
                       <Grid item>
                            <TextField className={classes.tf} label="Body" variant="filled"/>
                       </Grid>
                       <Grid item>
                            <SearchRoundedIcon></SearchRoundedIcon>
                       </Grid>
                       <Grid item></Grid>
                       <Grid item></Grid>
                       <Grid item>
                            <PrintRoundedIcon></PrintRoundedIcon>
                       </Grid>
                       <Grid item></Grid>
                       <Grid item></Grid>
                       <Grid item>
                            <VisibilityRoundedIcon></VisibilityRoundedIcon>
                       </Grid>
                       <Grid item>
                            <EditRoundedIcon></EditRoundedIcon>
                       </Grid>
                       <Grid item>
                            <DeleteRoundedIcon></DeleteRoundedIcon>
                       </Grid>
                       <Grid item>
                            <AddCircleRoundedIcon></AddCircleRoundedIcon>
                       </Grid>
                    </Grid>
                </Grid>
                <Grid item>
                    <Grid container direction="row" justifyContent="center" alignItems="center" spacing={4} >
                        <Grid item>
                            <ArrowBackIosTwoToneIcon></ArrowBackIosTwoToneIcon>
                        </Grid>
                        <Grid item>
                            <TableContainer component={Paper}>
                                <Table sx={{ minWidth: 650 }} aria-label="simple table">
                                    <TableHead>
                                    <TableRow>
                                        <TableCell> </TableCell>
                                        <TableCell>Service ID</TableCell>
                                        <TableCell>Vendor Name</TableCell>
                                        <TableCell>Route</TableCell>
                                        <TableCell>Date/Time</TableCell>
                                        <TableCell>Status</TableCell>
                                    </TableRow>
                                    </TableHead>
                                    <TableBody>
                                    {rows.map((row) => (
                                        <TableRow
                                        key={row.serviceID}
                                        sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                        >
                                        <TableCell>{row.tick}</TableCell>
                                        <TableCell>{row.serviceID}</TableCell>
                                        <TableCell>{row.vendorName}</TableCell>
                                        <TableCell>{row.route}</TableCell>
                                        <TableCell>{row.datetime}</TableCell>
                                        <TableCell>{row.status}</TableCell>
                                        </TableRow>
                                    ))}
                                    </TableBody>
                                </Table>
                            </TableContainer>
                        </Grid>
                        <Grid item>
                            <ArrowForwardIosRoundedIcon></ArrowForwardIosRoundedIcon>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
        </Box>
    );
}

export default Service

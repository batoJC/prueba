//imports
/********/
const express = require('express');
const mongoose = require('mongoose');
const config = require('config');
const ClientSchema = require('./models/ClientModel');
const bodyParser = require('body-parser');
const cors = require('cors');

//db config
/**********/
const dbServerInfo = config.get('mongoServer');
mongoose.connect(dbServerInfo,{ 
    useNewUrlParser: true, 
    useCreateIndex: true, 
    useFindAndModify: false })
.then(() => console.log('mongodb connected...'))
.catch(err => console.log('Error connecting: ' + err));


//server config
/**************/
const app = new express();
const port = 3000;
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const corsOptions = {
    origin: 'http://localhost:4200',
    optionsSuccessStatus: 200
}

app.use(cors(corsOptions));




//server routes
/**************/
app.listen(port,()=>{
    console.log('server stared');
});

//crear cliente
/**************/
// app.get('/api/client/create', (req, res) => {
//     console.log(req.body);
//     let newClient = new ClientSchema({
//         document:'78456',
//         name: 'Juan Carlos',
//         last_name: 'Giraldo Rios',
//         cellphone: '324324234',
//         address: 'direccion'
//     });
//     newClient.save()
//         .then(doc => {
//             console.log('document saved');
//             res.status(200).send(doc);
//         })
//         .catch(err => {
//             console.log('Error: ' + err);
//             res.status(500).send(err);
//         });
// });


//crear cliente
/**************/
app.post('/api/client', (req, res) => {
    console.log(req.body);
    let newClient = new ClientSchema(req.body);
    newClient.save()
        .then(doc => {
            console.log('document saved');
            res.status(200).send(doc);
        })
        .catch(err => {
            console.log('Error: ' + err);
            res.status(500).send(err);
        });
});

//buscar cliente por id
/**********************/
app.get('/api/client/:id', (req, res) => {
    let clientId = req.params.id;
    ClientSchema.findById(clientId)
        .then(item => {
            res.status(200).send(item);
        })
        .catch(err => {
            res.status(500).send('Error: ' + err);
        })
});

//lista de clientes
/******************/
app.get('/api/clientList', (req, res) => {
    ClientSchema.find()
        .then(items => {
            res.status(200).send(items);
        })
        .catch(err => {
            res.status(500).send('Error: ' + err);
        })
});

//actualizar un cliente
/**********************/
app.put('/api/client', (req, res) => {
    console.log(req.body);
    console.log('actualizando registro');
    ClientSchema.findByIdAndUpdate(req.body._id, req.body, { new: true })
        .then(doc => {
            console.log('document updated');
            res.status(200).send(doc);
        })
        .catch(err => {
            console.log('Error: ' + err);
            res.status(500).send(err);
        });
});


//eliminar un cliente
/*******************/
app.delete('/api/client/:id', (req, res) => {
    ClientSchema.findByIdAndDelete(req.params.id)
        .then(item => {
            console.log('car removed');
            res.status(200).send(true);
        })
        .catch(err => {
            console.log(err);
            res.status(500).send(false);
        })
});
const mongoose = require('mongoose');

const clientSchema = new mongoose.Schema({
 
    document:{
        type: String,
        required: true
    },
    name:{
        type: String,
        required: true
    },
    last_name:{
        type: String,
        required: false
    },
    cellphone:{
        type: String,
        required: false
    },
    address:{
        type: String,
        required: false
    }

});

const ClientModel = mongoose.model('Client_Coll', clientSchema);

module.exports = ClientModel;
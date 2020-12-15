const express = require('express')
const app = express()
const port = process.env.PORT || 8000
const cors = require('cors')
const path = require('path')
const { spawn } = require('child_process')
app.use(cors())

app.get('/p/:urlstring', function (req, res) {
    //gets name of website from params to send to python
    let url = req.params.urlstring
    console.log("Run Python...\n")
    const python = spawn('python3', ['../webScraper.py', url])
    python.stdout.on('data', (data) => {
        console.log(`data: ${data}`)
    })
    python.stderr.on('data', (data) => {
        console.log(`error: ${data}`)
    })
    python.on('close', () => {
        console.log("Closed")
    })
    //change this later to a route path
    res.redirect('/')
})

app.use(express.static('public'))

app.get('*', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'public', 'index.html'));
})

app.listen(port, () => {
    console.log(`Server is up at port ${port}`)
})

const express = require('express')
const app = express()
const port = process.env.PORT || 8000
const cors = require('cors')
const path = require('path')
const { spawn } = require('child_process')
app.use(cors())

app.get('/p/:urlstring', function (req, res) {
    console.log("in app.get")
    let url = req.params.urlstring
    const python = spawn('python3', ['webScraper.py', url])
    python.stdout.on('data', (data) => {
        console.log(`data: ${data}`)
    })
    python.stderr.on('data', (data) => {
        console.log(`error: ${data}`)
    })
    python.on('close', () => {
        console.log("Closed")
    })
    res.redirect('/')
})

app.use(express.static('public'))

app.get('*', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'public', 'index.html'));
})

app.listen(port, () => {
    console.log(`Server is up at port ${port}`)
})

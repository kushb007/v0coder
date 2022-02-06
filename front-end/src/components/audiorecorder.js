import React, { Component, useEffect } from 'react'

import axios from 'axios'; 
import { saveAs } from 'file-saver';
import AudioReactRecorder, { RecordState } from 'audio-react-recorder';
//import asyncHandler from "express-async-handler";
const asyncHandler = require("express-async-handler");
var async = require("async");

class AudioRecorder extends Component {
    
  constructor(props) {
    super(props)
 
    this.state = {
      recordState: null,
      completionState: false,
      go: null,
      id: null
    }
  }
 
  start = () => {
    this.setState({
      recordState: RecordState.START
    })
  }
 
  stop = () => {
    this.setState({
      recordState: RecordState.STOP
    })
  }
  primeApi =  (audioData) =>{
    
    const assembly = axios.create({
        baseURL: "https://api.assemblyai.com/v2",
        headers: {
            authorization: "d5086660044c456f8645a3a38e517c0b",
            "content-type": "application/json",
            
        },
    });

    assembly.post( "/upload", audioData['blob'])
    .then(  (res) => {
            console.log(res.data['upload_url']);
            assembly
            .post("/transcript", {
                audio_url: res.data['upload_url']
            }).then(
                (res) =>{
                    this.setState(
                        {
                            go:true
                        }
                    )
                   
                    // console.log("before");
                    // while (true){
                    //     assembly.get(  `/transcript/`+res.data['id']).then( (res) => {
                    //         console.log("retrieving results");
                    //         console.log(res.data);
                    //         if (res.data['text'] != null){
                    //             this.setState({
                    //                 completionState : true
                    //             })
                                
                    //             return res.data['text'];
                    //         }
                    //     });
                    // }
                    this.setState({
                        id: res.data['id']
                    })
                    return this.retrieveResults(res.data['id']);
                }
            )
        });
    // console.log(audioData);

  }

  retrieveResults =  async (jobId) =>{
    
    const assembly = axios.create({
        baseURL: "https://api.assemblyai.com/v2",
        headers: {
            authorization: "d5086660044c456f8645a3a38e517c0b",
            "content-type": "application/json",
            
        },
    });

    assembly.get( `/transcript/`+jobId).then( (res) => {
        console.log("retrieving results");
        if (res.data['text'] != null){
            this.setState({
                completionState : true,
                go : res.data['text']
            })
            //console.log(res.data);
            return res.data['text'];
        }
        else{
            setTimeout( () =>this.retrieveResults(jobId),5000);
        }
        
        
    });
  }
  componentDidUpdate(prevState){
        if (this.state.go != prevState.go){
         console.log("hello");
        }
  }
  
  //audioData contains blob and blobUrl
  onStop = async (audioData) => {
    console.log('audioData', audioData.blob);
    // var FileSaver = require('file-saver');
    // FileSaver.saveAs(audioData['blob'], "./a.wav");
    // const myFile = new File([audioData], "x.wav", {
    //     type: audioData.type,
    //   });
    // console.log(myFile);
    
    // this.primeApi(audioData).then(
    //     (id) =>{
    //         if (!this.completionState){
    //             setTimeout(this.retrieveResults(id), 5000);
    //         }
    //     }
    // );
    

    
    
    
    this.primeApi(audioData);    

   

    
    
   
    // assembly
    // .post("/upload", audioData['blob'])
    // .then((res) => {
    //     console.log(res.data['upload_url']);
    //     assembly
    //     .post("/transcript", {
    //         audio_url: res.data['upload_url']
    //     })
    //     .then((res) => {
    //         assembly.get(`/transcript/o6c27mn9dp-c035-4397-96c5-e474f2720718`)
    //         .then((res) => {
    //             if(res.data['status'] === 'queued'){
                    
    //                 assembly.get(`/transcript/o6c27mn9dp-c035-4397-96c5-e474f2720718`).then((res) => console.log(res.data))
    //             }
    //         });
    //     })
    //     .catch((err) => console.error(err));

    // }).catch((err) => console.error(err));


    
  }
 
  render() {
    const { recordState } = this.state
 
    return (
      <div>
        <AudioReactRecorder state={recordState} onStop={this.onStop} />
 
        <button onClick={this.start}>Start</button>
        <button onClick={this.stop}>Stop</button>
        <h1>{this.state.go}</h1>
      </div>
    )
  }
}

export default AudioRecorder;


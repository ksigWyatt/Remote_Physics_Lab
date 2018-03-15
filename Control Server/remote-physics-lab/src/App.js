import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {

    return (

        <div className="App">
            <div class="jumbotron">
            <h1 class="display-4">Remote Physics Lab</h1>
            <p class="lead">Helping students learn Physics from anyhere</p>
            </div>
        
            {/* YouTube Player for the stream */}
            <div class="card mb-3">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/rAlZRFZTwxM?rel=0&amp;controls=0&amp;showinfo=0" frameBorder="0" allow="autoplay; encrypted-media"></iframe>
                <div class="card-body">
                    <h5 class="card-title">Live Video</h5>
                    <br />
                    <button type="button" class="btn btn-primary">Request Access</button>
                    <p class="card-text"><small class="text-muted">X students waiting</small></p>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-6">
                    <div class="card border-light">
                    <div class="card-body">
                        <h5 class="card-title">Deflecting Voltage</h5>
                        <div class="slidecontainer">
                            <input id="volt-def-slider" type="range" min="50" max="250" step="1" value="0" class="slider"></input>
                            <p id="volt-def-value"></p>
                        </div>
                        <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-secondary">Positive</button>
                            <button type="button" class="btn btn-secondary">Off</button>
                            <button type="button" class="btn btn-secondary">Negative</button>
                        </div>
                    </div>
                    </div>
                </div> 
                <div class="col-sm-6">
                    <div class="card border-light">
                    <div class="card-body">
                        <h5 class="card-title">Magnetizing Current</h5>
                        
                        <div class="slidecontainer">
                            <input  id="curr-slider" type="range" min="0" value="0" max="3" step="0.05" class="slider"></input>
                            <p id="curr-value"></p>
                        </div>
                        <div class="btn-group" role="group" aria-label="Basic example">
                            <button type="button" class="btn btn-secondary">Clockwise</button>
                            <button type="button" class="btn btn-secondary">Off</button>
                            <button type="button" class="btn btn-secondary">Counter-CW</button>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
            <br />
            <div class="row">
                <div class="col-sm-6">
                    <div class="card border-light">
                    <div class="card-body">
                        <h5 class="card-title">Accelerating Voltage</h5>
                        {/* <slider></slider> */}
                        <div class="slidecontainer">
                        {/* TODO: Using the Library to create the sliders for react */}
                            <input id="volt-acc-slider" type="range" min="0" max="250" step="1" value="0" class="slider"></input>
                            <p id="volt-acc-value"></p>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
        </div>

        
    );
  }

  
}

export default App;
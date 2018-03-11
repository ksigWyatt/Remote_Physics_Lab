import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <h2>Remote Physics Lab</h2>
        
        <div class="row">
            <div class="column left1"></div>
            <div class="column middle1">
                <div id="video-feed" class="video">
                    <iframe src="_" frameborder="2"></iframe>
                    <h3>Live Video</h3>
                </div>
            </div>
            <div class="column right1"></div>
        </div>

        <br />
        <br />
        <br />

        <div id="controls" class="row">
            <button class="button">Request Access</button>
            <p id="queue">x students ahead of you</p>

            <br />
            <br />

            <h3>Controls</h3>
            <p id="alert-message"></p>
            <div class="centered">
                <button class="button">Reset</button>
                
            </div>
            
            <div class="two-row">
                <div class="two-column">
                    <h4>Accelerating Voltage</h4>

                    <div class="slidecontainer">
                        <input id="volt-acc-slider" type="range" min="0" max="250" step="1" value="0" class="slider"></input>
                        <p id="volt-acc-value"></p>
                    </div>

                    <br />
                    <br />

                    <h4>Deflecting Voltage</h4>
                    <div class="slidecontainer">
                        <input id="volt-def-slider" type="range" min="50" max="250" step="1" value="0" class="slider"></input>
                        <p id="volt-def-value"></p>
                        <p id="volt-selected-value">value of voltage button</p>
                    </div>

                    <br />
                    <br />

                    <div class="btn-group">
                        <button class="button-stack1">Positive</button>
                        <button class="button-stack1">Off</button>
                        <button class="button-stack1">Negative</button>
                    </div>
                </div>
                <div class="two-column">
                    <h4>Magnetizing Current</h4>

                    <div class="slidecontainer">
                        <input id="curr-slider" type="range" min="0" value="0" max="3" step="0.05" class="slider"></input>
                        <p id="curr-value"></p>
                        <p id="curr-selected-value">value of current button</p>
                    </div>
                    <br />
                    <br />
                    <h5 style="text-align: right;">Magnetic Arc</h5>
                    <div class="btn-group">
                        <button class="button-stack2">Clockwise</button>
                        <button class="button-stack2">Off</button>
                        <button class="button-stack2">Counter CW</button>
                    </div>
                </div>
            </div>
        </div>
      </div>
    );
  }
}

export default App;
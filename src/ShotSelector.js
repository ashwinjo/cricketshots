import React, { Component } from 'react';

class ShotSelector extends Component {
  constructor(props) {

    super(props);
    // State to store the selected string

    this.shots = [
        "Straight-Drive",
        "Cover Drive",
        "Square Drive",
        "Sweep",
        "Cut",
        "Late Cut",
        "Pull Shot",
        "Hook Shot",
        "Uppercut",
        "Switch Hit",
        "Dilcoop",
        "Reverse Scoop",
        "Paddle Scoop",
        "Reverse Sweep",
        "Slog Sweep",
        "Square Cut",
        "Ramp Shot"
    ]

    this.legside = [
        "Sweep",
        "Dilcoop",
        "Paddle Scoop",
        "Slog Sweep",
        "Ramp Shot",
        "Pull Shot",
        "Hook Shot",
        "Switch Hit",
    ]


    this.offside = [
        "Straight-Drive",
        "Cover Drive",
        "Square Drive",
        "Cut",
        "Late Cut",
        "Uppercut",
        "Square Cut",
        "Reverse Sweep",
    ]



    this.state = {
      selectedString: 'No Shot Selected',
    };


    // Bind the event handler to the class instance
    this.handleDropdownChange = this.handleDropdownChange.bind(this);
  }

  // Event handler for dropdown change
  handleDropdownChange(e) {
    console.log(this.state.selectedString)
    this.val = e.target.value;

    this.offsideBool = this.offside.includes(this.val);
    this.legsideBool = this.legside.includes(this.val);

    if (this.offsideBool){
        this.val = "Off Side"
    }

    if (this.legsideBool){
        this.val = "Leg Side"
    }

    this.setState({
        selectedString: e.target.value,
    });

    //Callback parent compoenet with the value
    this.props.onDropdownChange(this.val);
  }

  // List of strings for the dropdown
  stringOptions = this.props.shots

  render() {
    console.log(this.state.selectedString)
    return (
      <div>
        <label htmlFor="dropdown" className="ui huge label">Select your shot: </label>
        <select
          id="dropdown"
          value={this.state.selectedString}
          onChange={this.handleDropdownChange}
          className="ui dropdown"
        >
          <option value="">Select an option</option>
          {this.shots.map((option, index) => (
            <option key={index} value={option}>
              {option}
            </option>
          ))}
        </select>
        <br/><br/>
        <div><label className="ui huge red label"> You have Selected:</label>{this.state.selectedString && (
          <label className="ui huge green label">{this.state.selectedString}</label>
        )}</div>
        
      </div>
    );
  }
}

export default ShotSelector;

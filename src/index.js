import React from 'react';
import ReactDOM from 'react-dom';
import ShotSelector from './ShotSelector';
import cricket from './cricket.jpg'



class App extends React.Component {

  constructor(props){
    super(props)
    this.state = { resultSide: null }
  }

  handleDropdownChange = (value) => {
    this.setState({resultSide: value});
  };

  componentDidMount() {
    // Update the state after component is mounted
    setTimeout(() => {
      this.setState({ resultSide: "No Side"});
    }, 2000); // Update after 2 seconds (adjust as needed)
  }
  
  render() {
  console.log(this.state.resultSide)
  return (
    <div className="ui container">
      <div class="ui inverted segment">
          <div class="ui inverted secondary menu">

            <label className="ui huge blue label">Off OR Leg</label>
            
          </div>
    </div>
      <ShotSelector onDropdownChange={this.handleDropdownChange}/>  
      <br/>
      <div><h1 className="ui header">Pitch Side: <label className="ui huge green label">{this.state.resultSide}</label></h1></div>
      <br/>
      <div>
        <img className="ui big fluid image" src={cricket}/>
      <div/>
    </div>
  </div>

  );
}
}

ReactDOM.render(
  <App/>,
  document.querySelector("#root")
)


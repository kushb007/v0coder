import RecorderJSDemo from "./components/recorder";

'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}

function App() {
  return (
    <div className="App">
      <RecorderJSDemo></RecorderJSDemo>
    </div>
  );
}

export default App;

const domContainer = document.querySelector('#react');
ReactDOM.render(e(LikeButton), domContainer);

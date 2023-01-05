import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Search from './components/Search';
import gplayLogo from './components/logo.png'

function App() {
  return (
  <>
    <div className="container d-flex justify-content-between align-items-center">
      <img src={gplayLogo} style={{ width: "20rem", position: "relative", left: "38%", cursor: "pointer" }} alt="" />
    </div>
   <Search />
  </>
  );
}

export default App;
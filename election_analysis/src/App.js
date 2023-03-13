
import React, { useState } from 'react';
import axios from 'axios';
<<<<<<< Updated upstream
=======
import './App.css'


>>>>>>> Stashed changes

function QueryForm() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    //console.log("the query being sent" + query)
    //const url = '/query-csv/?query=' + encodeURIComponent(query);
	//const url = 'http://localhost:8000/query-csv/?query=' + encodeURIComponent(query);
	const url = 'http://127.0.0.1:8000/query-csv/?query=' + encodeURIComponent(query);
	//console.log(url)
    try {
      const response = await axios.get(url);
<<<<<<< Updated upstream
	  console.log(response)
	  setResponse(response.data.result);
=======
	  console.log(response);
	  setResponse(response.data.result);
    setQuery('');
>>>>>>> Stashed changes
      //setResponse(response.data.result[0][1]);  this is to get value of each column separately 
    } catch (error) {
      console.error(error);
      setResponse('error');
    }
  };

  return (
<<<<<<< Updated upstream
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Query:
          <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} />
        </label>
        <button type="submit">Submit</button>
      </form>
      {response !== null && (
        <p>Response: {response}</p>
      )}
    </div>
=======
    <div className='main'>
      <div className='blue-part'>
      <div className='search'>
      <form onSubmit={handleSubmit}>
        <i className="fa fa-search" aria-hidden="true"></i>
        <input className="query_inp" placeholder="Write your query here" type="text" value={query} onChange={(e) => setQuery(e.target.value)} />
        <button className="btn" type="submit">Submit</button>
      </form> 
      </div>
      <div className='filter'>
        <p>Filter 1</p><br></br>
        <p>Filter 2</p><br></br>
        <p>Filter 3</p>
      </div>
      {/* <div className='response'>
  {response !== null && (
    <div>
      {response.map((row, rowIndex) => (
        <div key={rowIndex}>
          {row.map((col, colIndex) => (
            <span key={colIndex}>{col}</span>
          ))}
        </div>
      ))}
    </div>
  )}
</div> */}

      <div className='response'>
      {response !== null && (
        <table className='table table-stripped'>
              <thead className='thead-dark'>
                <tr>
                  <th scope='col'>ID</th>
                  <th scope='col'>Tweet</th>
                  <th scope='col'>State</th>
                  <th scope='col'>Sentiment Analysis 1</th>
                  <th scope='col'>Polarity</th>
                </tr>
              </thead>
              <tbody>
                {response.map((row, rowindex) => (
                  <tr key={rowindex}>
                    {row.map((col, index) => {
                      let cssClass = '';
                    if ((index === 3 || index===4) && col === 'Y') {
                    cssClass = 'positive';
                     } else if ((index === 3 || index===4) && col === 'N') {
                      cssClass = 'negative';
                    }
                    const columnCssClass = `column-${index + 1}`;
                    const combinedCssClass = `${columnCssClass} ${cssClass}  `;
                    
                      return <td key={index} className={combinedCssClass} >{col}</td>
                      
                    })}
                  </tr>
                ))}
              </tbody>
            </table>

            
        
      )}
    </div>
      </div>
      <div className='yellow-part'></div>
    </div>
>>>>>>> Stashed changes
  );
}

export default QueryForm;








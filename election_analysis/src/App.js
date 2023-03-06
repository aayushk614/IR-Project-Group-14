
import React, { useState } from 'react';
import axios from 'axios';

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
	  console.log(response)
	  setResponse(response.data.result);
      //setResponse(response.data.result[0][1]);  this is to get value of each column separately 
    } catch (error) {
      console.error(error);
      setResponse('error');
    }
  };

  return (
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
  );
}

export default QueryForm;








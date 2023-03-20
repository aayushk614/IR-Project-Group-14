
import React, { useState } from 'react';
import axios from 'axios';
import './App.css'

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" 
integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" 
crossorigin="anonymous"></link>

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
	  console.log(response);
	  setResponse(response.data.result);
    setQuery('');
      //setResponse(response.data.result[0][1]);  this is to get value of each column separately 
    } catch (error) {
      console.error(error);
      setResponse('error');
    }
  };

  return (
    <div className='container-fluid '>
      <div className='main'>
        <div className='blue-part'>
          
          <div className='search'>
            <form onSubmit={handleSubmit}>
              <i className="fa fa-search" aria-hidden="true"></i>
              <input className="query_inp" placeholder="Write your query here" type="text" value={query} onChange={(e) => setQuery(e.target.value)} />
              <button className="btn" type="submit">Submit</button>
            </form> 
          </div>
          <div className='row'>
            <div className='filter col-xs-3 col-sm-3 col-md-3 col-lg-3'>
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

            <div className='response col-xs-8 col-sm-8 col-md-8 col-lg-8'>
            
              {response !== null && (
                <table className='table table-stripped'>
                      <thead className='thead-dark'>
                        {/*<tr>
                          <th scope='col'>ID</th>
                          <th scope='col'>Tweet</th>
                          <th scope='col'>State</th>
                          <th scope='col'>Sentiment Analysis 1</th>
                          <th scope='col'>Polarity</th>
              </tr>*/}
                      </thead>
                      <tbody>
                      {response.map((row, rowindex) => (
                        <tr className='tr_style' key={rowindex}>
                          
                          <td colspan = "5">
                            <tr>
                              <td className='border_style' rowspan = "2">
                                {row[0]}
                              </td>
                              <td className='td_style' colspan = "4">
                                {row[1]}
                              </td>
                            </tr>
                            <tr>
                              <td className='width_style1'>
                                <button className='button_style1'> 
                                {row[2]}
                                
                                  
                                </button>
                              </td>
                              <td className='width_style2'>
                                <button className='button_style'> 
                                  
                                  {row[3]}
                                </button> 
                              </td>
                              <td className='width_style2'>
                                <button className='button_style'> 
                                  {row[4]}
                                </button>
                              </td>
                            </tr> 
                          </td>
                        </tr>
                      ))}
                        {/*{response.map((row, rowindex) => (
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
                          ))}*/}
                      </tbody>
                    </table>     
                
              )}
          
            </div>
          </div>
        </div>
      </div>
        <div className='yellow-part'></div>
    </div>
  );
}

export default QueryForm;








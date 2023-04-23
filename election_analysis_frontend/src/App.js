
import React, { useState } from 'react';
import axios from 'axios';
import './App.css'

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" 
integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" 
crossorigin="anonymous"></link>

function QueryForm() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);

  const [isChecked1, setIsChecked1] = useState(false);
  const [isChecked2, setIsChecked2] = useState(false);
  const [isChecked3, setIsChecked3] = useState(false);
  const [selectedOption, setSelectedOption] = useState(null);
  const [filteredResponse, setFilteredResponse] = useState(null);

  const dropdownOptions = ['Delhi' , 'Maharashtra' , 'Andhra Pradesh' ,'Karnataka' ,'Bihar' ,'West Bengal',
  'Assam' ,'Tamil Nadu', 'Uttar Pradesh' ,'Madhya Pradesh', 'Chandigarh',
  'Jharkhand', 'Gujarat', 'Kerala', 'Haryana' ,'Rajasthan', 'Punjab',
  'Jammu & Kashmir', 'Goa' ,'Chhattisgarh' ,'Orissa', 'Tripura', 'Telangana',
  'Mizoram', 'Daman & Diu', 'Uttaranchal' ,'Nagaland', 'Pondicherry', 'Manipur',
  'Arunachal Pradesh', 'Andaman & Nicobar Islands' ,'Himachal Pradesh',
  'Sikkim' ,'Meghalaya'];
  const handleDropdownChange = (event) => {
    setSelectedOption(event.target.value);
  }

  

  const handleCheckboxChange1 = () => {
    setIsChecked1(!isChecked1);
  };

  const handleCheckboxChange2 = () => {
    setIsChecked2(!isChecked2);
  };

  const handleCheckboxChange3 = () => {
    setIsChecked3(!isChecked3);
  };
  
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
    setFilteredResponse(response.data.result);
    setQuery('');
      //setResponse(response.data.result[0][1]);  this is to get value of each column separately 
    } catch (error) {
      console.error(error);
      setResponse('error');
    }
  };
  const handleFilter = () => {
    
    let filteredData = response;
  
    // Apply filter based on selectedOption
    if (selectedOption) {
      filteredData = filteredData.filter(row => row[2] === selectedOption);
    }
  
    // Apply filter based on checkboxes
    const selectedParties = [];
    if (isChecked1) {
      selectedParties.push("BJP");
    }
    if (isChecked2) {
      selectedParties.push("Congress");
    }
    if (isChecked3) {
      selectedParties.push("Other");
    }
  
    if (selectedParties.length > 0) {
      filteredData = filteredData.filter(row => selectedParties.includes(row[5]));
    }
  
    // Set filtered data
    setFilteredResponse(filteredData);
    };

  return (
    <div className='container-fluid '>
      <div className='main'>
        <div className='blue-part'>
          <div className='row'>

            <div className='summary col-xs-2 col-sm-2 col-md-2 col-lg-2'>
              <a target= '_blank' href='http://localhost:8501'>
                <button className='summary_button'>
                  Sentiment 
                </button>
              </a>
            </div>

            <div className='summary1 col-xs-2 col-sm-2 col-md-2 col-lg-2'>
              <a target= '_blank' href='http://localhost:8502'>
                <button className='summary_button'>
                  Manipulation
                </button>
              </a>
            </div>
            

            <div className='search  col-xs-6 col-sm-6 col-md-6 col-lg-6'>
              <form onSubmit={handleSubmit}>
                <i className="fa fa-search" aria-hidden="true"></i>
                <input className="query_inp" placeholder="Write your query here" type="text" value={query} onChange={(e) => setQuery(e.target.value)} />
                <button className="btn" type="submit">Submit</button>
              </form> 
            </div>

          </div>
          <div className='row'>
            <div className='filter col-xs-3 col-sm-3 col-md-3 col-lg-3'>
           
              <label className='label_style' htmlFor='dropdown'>Location :</label>
              <select className='dropdown_state' id='dropdown' value={selectedOption} onChange={handleDropdownChange}>
                <option value=''>Select an option</option>
                {dropdownOptions.map((option) => (
                <option key={option} value={option}>{option}</option>
                ))}
              </select>
              <label className='label_style' >Political Parties :
                <label className="container label_style_text">
                  <input className='checkbox_style' type="checkbox" checked={isChecked1} onChange={handleCheckboxChange1}/>
                  <span class="checkmark"></span>BJP 
                </label>
                <label className="container label_style_text">
                  <input className='checkbox_style' type="checkbox" checked={isChecked2} onChange={handleCheckboxChange2}/>
                    Congress
                  <span class="checkmark"></span>
                </label>
                <label className="container label_style_text">
                  <input className='checkbox_style' type="checkbox" checked={isChecked3} onChange={handleCheckboxChange3}/>
                    Other
                  <span class="checkmark"></span>
                </label>
              </label>
                <div className='b'><button className="btn1" type="submit"  onClick={handleFilter}>Filter</button></div>

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
            
              {filteredResponse && (
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
                      {filteredResponse.map((row, rowindex) => (
                        <tr className='tr_style' key={rowindex}>
                          {rowindex !== response.length - 1 ?

                            <td colspan = "5">
                              <tr>
                                <td className='border_style' rowspan = "2">
                                  <span >{rowindex+1}</span><br></br><br></br>
                                  <span className='row_count_style'>{row[0]}</span>
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
                                <td className='width_style1'>
                                  <button className='button_style1'>
                                    {row[5]}
                                  </button>
                                </td>
                                <td className='width_style1'>
                                  <button className='button_style1'>
                                    {row[6]}
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
                            </td>:null
                          }
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
           
              <br></br><br></br>
              {response !== null && (
                <table className='table table-stripped table_border'> 
                  <caption>Similarity Matrix of tweets</caption>
                    <thead>
                      <tr className='tr_similarity_header'>
                        {response[response.length - 1][0].map((colHeader, index) => (
                          index > 0 ? <th key={index}>{index}</th> : <th key={index}> </th>
                        
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {response[response.length - 1].map((col, index) => (
                        <tr key={index} className = 'similarity_table tr_similarity'>
                          
                          {col.map((val, subIndex) => (
                            <td key={subIndex}>{val}</td>
                          ))}
                        </tr>
                      ))}
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








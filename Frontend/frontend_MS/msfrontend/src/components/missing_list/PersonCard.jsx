import React from 'react';

const PersonCard = (props) => {

  const deletethis = async (id) => {
    const response = await fetch(`http://localhost:5000/api/missingpeople/deleteperson/${id}`, {
      method: 'DELETE',
    });
    const json = await response.json();
    const responsestatus = response.status;
    if (responsestatus === 200) {
      alert(`person having adhaar number ${id} deleted successfully`);
    }
    const newcases = props.totalcases.filter((noteelement) => noteelement.adhaar_number !== id);
    props.changecase(newcases);
  };

  return (
    <article className="card-person">
      <div className="avatar">
        <img src={props.image} alt={props.name} />
      </div>

      <div className="meta">
        <h3>{props.name} <small style={{color:'var(--muted)',marginLeft:8,fontWeight:600}}>{props.gender}</small></h3>
        <div className="muted">{props.address}</div>
        <div className="facts">
          <div className="fact-pill">Missing: {props.date}</div>
          <div className="fact-pill">Height: {props.height}</div>
          <div className="fact-pill">ID: {props.identification}</div>
        </div>
      </div>

      <div className="card-actions">
        <button className="btn btn-danger" onClick={() => window.alert('Contact owner feature coming soon')}>Contact</button>
        <button className="btn btn-danger" onClick={() => deletethis(props.adhaar)}>Delete</button>
      </div>
    </article>
  );
};

export default PersonCard;
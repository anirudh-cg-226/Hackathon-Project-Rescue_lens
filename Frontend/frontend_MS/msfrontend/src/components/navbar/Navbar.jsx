import React, { useState } from 'react';
import applogo from './applogo.png';
import { Link } from 'react-router-dom';

const Navbar = () => {
    const [open, setOpen] = useState(false);
    return (
        <header className="app-navbar">
            <div className="brand">
                <div className="logo">FL</div>
                <div className="title">FindOne</div>
            </div>

            <nav>
                <ul style={{display: open ? 'flex' : undefined}}>
                    <li><Link to="/">Home</Link></li>
                    <li><a href="http://localhost:8501/" target="_blank" rel="noreferrer">Surveillance</a></li>
                    <li><Link to="/Formmissing">Report</Link></li>
                    <li><Link to="/Missingpeople">Missing List</Link></li>
                    <li><Link to="/locations">Locations</Link></li>
                </ul>
            </nav>

            <div style={{display:'flex',alignItems:'center',gap:12}}>
                <button className="cta" onClick={()=>window.location.href='/Formmissing'}>Report case</button>
                <button aria-label="menu" onClick={()=>setOpen(!open)} style={{background:'transparent',border:0,color:'var(--muted)',fontSize:20}}>
                    {open ? '✕' : '☰'}
                </button>
            </div>
        </header>
    );
};

export default Navbar;
import React from 'react';
import heroimg from './heroimagefinal.png';

const Index = () => {
    return (
        <main>
            <section className="hero-section">
                <div className="hero-left">
                    <div className="hero-eyebrow">We're here to help</div>
                    <h1 className="hero-title">Find missing people faster using smart recognition</h1>
                    <p className="hero-copy">A lightweight tool combining location, reports and image-matching to help communities reunite safely.</p>
                    <div style={{marginTop:20,display:'flex',gap:12}}>
                        <a className="btn btn-primary" href="/Missingpeople">Browse Cases</a>
                        <a className="btn btn-danger" href="/Formmissing">Report a case</a>
                    </div>
                </div>

                <div className="hero-visual">
                    <img src={heroimg} alt="hero visual" />
                </div>
            </section>
        </main>
    );
};

export default Index;

import streamlit as st

# Load the HTML content into Streamlit
html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #1a1a1a;
            max-width: 210mm;
            margin: 0 auto;
            background: #ffffff;
        }
        .cover {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background: linear-gradient(45deg, #0A2647 0%, #144272 100%);
            color: white;
            position: relative;
            overflow: hidden;
        }
        .logo {
            width: 120px;
            height: 120px;
            margin-bottom: 2rem;
            background: #C6A962;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            color: white;
        }
        .blockchain-bg {
            position: absolute;
            width: 100%;
            height: 100%;
            opacity: 0.1;
            pointer-events: none;
        }
        .section {
            padding: 3rem 2rem;
            margin: 1rem 0;
            background: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .service-card {
            background: #f8f9fa;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 4px solid #C6A962;
        }
        .process-step {
            display: flex;
            align-items: center;
            margin: 1rem 0;
        }
        .step-number {
            width: 40px;
            height: 40px;
            background: #0A2647;
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 1rem;
        }
        .testimonial {
            font-style: italic;
            padding: 1rem;
            border-left: 3px solid #C6A962;
            margin: 1rem 0;
            background: #f8f9fa;
        }
        .contact {
            background: #0A2647;
            color: white;
            padding: 2rem;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="cover">
        <svg class="blockchain-bg" viewBox="0 0 1000 1000">
            <pattern id="blockchainPattern" x="0" y="0" width="100" height="100" patternUnits="userSpaceOnUse">
                <circle cx="50" cy="50" r="2" fill="white"/>
                <line x1="50" y1="50" x2="150" y2="50" stroke="white" stroke-width="0.5"/>
                <line x1="50" y1="50" x2="50" y2="150" stroke="white" stroke-width="0.5"/>
            </pattern>
            <rect width="100%" height="100%" fill="url(#blockchainPattern)"/>
        </svg>
        
        <div class="logo">CE</div>
        <h1>Premium OTC Crypto Services</h1>
        <h3>Superior Liquidity · Guaranteed Confidentiality · Dedicated Expertise</h3>
    </div>

    <div class="section">
        <p>CryptoElite combines financial expertise and cutting-edge technology to redefine the standards of OTC crypto transactions. We provide tailor-made solutions to meet our clients' unique needs, offering global liquidity with unmatched precision and confidentiality.</p>
    </div>

    <div class="section">
        <h2>Our Services</h2>
        <div class="service-card">
            <h3>Instant Liquidity</h3>
            <p>Direct and secure access to global liquidity sources, optimized for large volume transactions.</p>
        </div>
        <div class="service-card">
            <h3>Absolute Confidentiality</h3>
            <p>Advanced protocols to safeguard data and ensure anonymity.</p>
        </div>
        <div class="service-card">
            <h3>Dedicated Expertise</h3>
            <p>A team of experienced consultants available 24/7 for personalized assistance.</p>
        </div>
        <div class="service-card">
            <h3>Multi-Currency Support</h3>
            <p>Support for major cryptocurrencies and flexible fiat conversions.</p>
        </div>
    </div>

    <div class="section">
        <h2>Transaction Process</h2>
        <div class="process-step">
            <div class="step-number">1</div>
            <div>
                <h3>Contact and Validation</h3>
                <p>Start the collaboration with a rigorous KYC validation process.</p>
            </div>
        </div>
        <div class="process-step">
            <div class="step-number">2</div>
            <div>
                <h3>Detail Definition</h3>
                <p>Define transaction parameters and receive advanced consultation.</p>
            </div>
        </div>
        <div class="process-step">
            <div class="step-number">3</div>
            <div>
                <h3>Offer Confirmation</h3>
                <p>Receive competitive real-time quotes.</p>
            </div>
        </div>
        <div class="process-step">
            <div class="step-number">4</div>
            <div>
                <h3>Discreet Finalization</h3>
                <p>Rapid settlement and secure fund delivery.</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2>Testimonials</h2>
        <div class="testimonial">
            <p>"CryptoElite provided us with fast access to liquidity solutions for complex transactions. The team's professionalism is outstanding."</p>
            <small>— Investment Director, Private Fund</small>
        </div>
        <div class="testimonial">
            <p>"CryptoElite is the ideal partner for high-volume transactions in a secure and confidential environment. Highly recommended!"</p>
            <small>— CEO, Tech Company</small>
        </div>
    </div>

    <div class="contact">
        <h2>Contact</h2>
        <p>Phone: +40 721 720 155</p>
        <p>Email: office@cryptoelite.com</p>
        <p>Website: www.cryptoelite.com</p>
        <img src="/api/placeholder/200/200" alt="QR Code" />
    </div>
</body>
</html>
"""
st.markdown(html_content, unsafe_allow_html=True)

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    background-color: #f5f5f5;
    font-family: 'Nunito', sans-serif;
    display: grid;
    grid-template-rows: auto 1fr auto;
    grid-template-areas: 
        "header"
        "main"
        "footer";
    line-height: 1.6;
    color: #333;
}

.header {
    grid-area: header;
    background: linear-gradient(135deg, #4a4a4a, #2c3e50);
    color: white;
    text-align: center;
    padding: 1.5rem 0;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.header h1 {
    font-size: 2.2rem;
    margin-bottom: 1rem;
    font-weight: 700;
    letter-spacing: 1px;
}

.menu {
    display: flex;
    justify-content: center;
    list-style: none;
    gap: 2rem;
    font-size: 1.1rem;
}

.menu-link {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    text-decoration: none;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: all 0.3s ease;
}

.menu-link:hover {
    background-color: rgba(255, 255, 255, 0.2);
    transform: translateY(-2px);
}

.seccion {
    grid-area: main;
    width: 90%;
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    background: white;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.seccion h2 {
    font-size: 1.8rem;
    color: #2c3e50;
    margin-bottom: 1rem;
    text-align: center;
}

.seccion p {
    text-align: center;
    margin-bottom: 2rem;
    color: #555;
}

.fieldset {
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    padding: 2rem;
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
}

.tileDatos {
    grid-column: 1 / -1;
    font-size: 1.3rem;
    color: #2c3e50;
    margin-bottom: 0.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #e0e0e0;
}

label {
    font-weight: 600;
    color: #444;
    display: block;
    margin-bottom: 0.5rem;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-family: 'Nunito', sans-serif;
    font-size: 1rem;
    transition: border 0.3s ease;
}

input[type="text"]:focus,
input[type="email"]:focus,
textarea:focus {
    border-color: #3498db;
    outline: none;
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2);
}

textarea {
    min-height: 150px;
    resize: vertical;
}

small {
    display: block;
    font-size: 0.8rem;
    color: #777;
    margin-top: -1rem;
    margin-bottom: 1rem;
}

.btn-enviar {
    background: linear-gradient(135deg, #3498db, #2980b9);
    color: white;
    border: none;
    padding: 1rem 2rem;
    font-size: 1rem;
    font-weight: 600;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.btn-enviar:hover {
    background: linear-gradient(135deg, #2980b9, #3498db);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.footer {
    grid-area: footer;
    background: linear-gradient(135deg, #4a4a4a, #2c3e50);
    color: white;
    text-align: center;
    padding: 1.5rem 0;
    display: grid;
    gap: 1rem;
}

.footer p {
    margin: 0.3rem 0;
}

.footer a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer a:hover {
    color: #2980b9;
    text-decoration: underline;
}

/* Estilos responsivos */
@media (max-width: 768px) {
    .menu {
        flex-direction: column;
        gap: 1rem;
        align-items: center;
    }
    
    .seccion {
        width: 95%;
        padding: 1.5rem;
    }
    
    .fieldset {
        padding: 1.5rem;
    }
}

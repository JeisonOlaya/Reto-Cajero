/* Media Queries para Responsive - Sobre Mi */
@media (max-width: 1200px) {
    .seccion {
        width: 80%;
    }
}

@media (max-width: 992px) {
    .seccion {
        width: 85%;
        margin: 40px auto;
    }
    .imgSobreMi {
        width: 250px;
    }
}

@media (max-width: 768px) {
    .menu {
        flex-direction: column;
        align-items: center;
        gap: 15px;
    }
    .seccion {
        width: 90%;
        padding: 30px;
    }
    .imgSobreMi {
        width: 200px;
    }
}

@media (max-width: 576px) {
    .header h1 {
        font-size: 1.8rem;
    }
    .seccion {
        width: 95%;
        padding: 20px;
    }
    .seccion h2 {
        font-size: 1.5rem;
    }
    .imgSobreMi {
        width: 180px;
    }
}

@media (max-width: 400px) {
    .header h1 {
        font-size: 1.6rem;
    }
    .menu {
        font-size: 18px;
        gap: 10px;
    }
    .seccion {
        padding: 15px;
    }
    .seccion h2 {
        font-size: 1.3rem;
    }
    .imgSobreMi {
        width: 150px;
    }
}

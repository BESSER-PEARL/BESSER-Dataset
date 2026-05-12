




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Biblioteca_Prestamo  {

    private LocalDate fechaDeFin;
    private LocalDate fechaDeInicio;
    private LocalDate fechaDeDevolucion;





    private Biblioteca_Socio biblioteca_socio;




    private Biblioteca_Socio biblioteca_socio;


    public Biblioteca_Prestamo(
        LocalDate fechaDeFin,        LocalDate fechaDeInicio,        LocalDate fechaDeDevolucion    ) {
        this.fechaDeFin = fechaDeFin;
        this.fechaDeInicio = fechaDeInicio;
        this.fechaDeDevolucion = fechaDeDevolucion;
    }


    public LocalDate getFechadefin() {
        return fechaDeFin;
    }

    public void setFechadefin(LocalDate fechaDeFin) {
        this.fechaDeFin = fechaDeFin;
    }
    public LocalDate getFechadeinicio() {
        return fechaDeInicio;
    }

    public void setFechadeinicio(LocalDate fechaDeInicio) {
        this.fechaDeInicio = fechaDeInicio;
    }
    public LocalDate getFechadedevolucion() {
        return fechaDeDevolucion;
    }

    public void setFechadedevolucion(LocalDate fechaDeDevolucion) {
        this.fechaDeDevolucion = fechaDeDevolucion;
    }

    public Biblioteca_Socio getBiblioteca_socio() {
        return biblioteca_socio;
    }

    public void setBiblioteca_socio(Biblioteca_Socio biblioteca_socio) {
        this.biblioteca_socio = biblioteca_socio;
    }
    public Biblioteca_Socio getBiblioteca_socio() {
        return biblioteca_socio;
    }

    public void setBiblioteca_socio(Biblioteca_Socio biblioteca_socio) {
        this.biblioteca_socio = biblioteca_socio;
    }

}
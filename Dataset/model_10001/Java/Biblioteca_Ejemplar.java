





import java.util.List;
import java.util.ArrayList;

public class Biblioteca_Ejemplar  {

    private String estado;
    private int numeroDeEjemplar;





    private Biblioteca_Prestamo biblioteca_prestamo;


    public Biblioteca_Ejemplar(
        String estado,        int numeroDeEjemplar    ) {
        this.estado = estado;
        this.numeroDeEjemplar = numeroDeEjemplar;
    }


    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }
    public int getNumerodeejemplar() {
        return numeroDeEjemplar;
    }

    public void setNumerodeejemplar(int numeroDeEjemplar) {
        this.numeroDeEjemplar = numeroDeEjemplar;
    }

    public Biblioteca_Prestamo getBiblioteca_prestamo() {
        return biblioteca_prestamo;
    }

    public void setBiblioteca_prestamo(Biblioteca_Prestamo biblioteca_prestamo) {
        this.biblioteca_prestamo = biblioteca_prestamo;
    }

}
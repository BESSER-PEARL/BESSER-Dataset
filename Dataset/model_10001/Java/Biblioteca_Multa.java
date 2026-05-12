




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Biblioteca_Multa  {

    private int monto;
    private LocalDate fecha;
    private int diasExcedidos;
    private LocalDate fechaDePago;





    private Biblioteca_Prestamo biblioteca_prestamo;




    private Biblioteca_Socio biblioteca_socio;


    public Biblioteca_Multa(
        int monto,        LocalDate fecha,        int diasExcedidos,        LocalDate fechaDePago    ) {
        this.monto = monto;
        this.fecha = fecha;
        this.diasExcedidos = diasExcedidos;
        this.fechaDePago = fechaDePago;
    }


    public int getMonto() {
        return monto;
    }

    public void setMonto(int monto) {
        this.monto = monto;
    }
    public LocalDate getFecha() {
        return fecha;
    }

    public void setFecha(LocalDate fecha) {
        this.fecha = fecha;
    }
    public int getDiasexcedidos() {
        return diasExcedidos;
    }

    public void setDiasexcedidos(int diasExcedidos) {
        this.diasExcedidos = diasExcedidos;
    }
    public LocalDate getFechadepago() {
        return fechaDePago;
    }

    public void setFechadepago(LocalDate fechaDePago) {
        this.fechaDePago = fechaDePago;
    }

    public Biblioteca_Prestamo getBiblioteca_prestamo() {
        return biblioteca_prestamo;
    }

    public void setBiblioteca_prestamo(Biblioteca_Prestamo biblioteca_prestamo) {
        this.biblioteca_prestamo = biblioteca_prestamo;
    }
    public Biblioteca_Socio getBiblioteca_socio() {
        return biblioteca_socio;
    }

    public void setBiblioteca_socio(Biblioteca_Socio biblioteca_socio) {
        this.biblioteca_socio = biblioteca_socio;
    }

}
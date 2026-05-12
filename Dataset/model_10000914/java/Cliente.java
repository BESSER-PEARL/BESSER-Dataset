




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Cliente  {

    private int idDireccion;
    private LocalDate fechaInicio;
    private String contactoReferencia;
    private int idPersona;
    private int idDiaPago;
    private int idAval;
    private int idCliente;
    private int idPrestamo;
    private String noTarjeta;



    public Cliente(
        int idDireccion,        LocalDate fechaInicio,        String contactoReferencia,        int idPersona,        int idDiaPago,        int idAval,        int idCliente,        int idPrestamo,        String noTarjeta    ) {
        this.idDireccion = idDireccion;
        this.fechaInicio = fechaInicio;
        this.contactoReferencia = contactoReferencia;
        this.idPersona = idPersona;
        this.idDiaPago = idDiaPago;
        this.idAval = idAval;
        this.idCliente = idCliente;
        this.idPrestamo = idPrestamo;
        this.noTarjeta = noTarjeta;
    }


    public int getIddireccion() {
        return idDireccion;
    }

    public void setIddireccion(int idDireccion) {
        this.idDireccion = idDireccion;
    }
    public LocalDate getFechainicio() {
        return fechaInicio;
    }

    public void setFechainicio(LocalDate fechaInicio) {
        this.fechaInicio = fechaInicio;
    }
    public String getContactoreferencia() {
        return contactoReferencia;
    }

    public void setContactoreferencia(String contactoReferencia) {
        this.contactoReferencia = contactoReferencia;
    }
    public int getIdpersona() {
        return idPersona;
    }

    public void setIdpersona(int idPersona) {
        this.idPersona = idPersona;
    }
    public int getIddiapago() {
        return idDiaPago;
    }

    public void setIddiapago(int idDiaPago) {
        this.idDiaPago = idDiaPago;
    }
    public int getIdaval() {
        return idAval;
    }

    public void setIdaval(int idAval) {
        this.idAval = idAval;
    }
    public int getIdcliente() {
        return idCliente;
    }

    public void setIdcliente(int idCliente) {
        this.idCliente = idCliente;
    }
    public int getIdprestamo() {
        return idPrestamo;
    }

    public void setIdprestamo(int idPrestamo) {
        this.idPrestamo = idPrestamo;
    }
    public String getNotarjeta() {
        return noTarjeta;
    }

    public void setNotarjeta(String noTarjeta) {
        this.noTarjeta = noTarjeta;
    }


}
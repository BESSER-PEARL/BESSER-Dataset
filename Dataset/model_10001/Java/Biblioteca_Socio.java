




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Biblioteca_Socio  {

    private int edad;
    private String nombreCompleto;
    private String telefono;
    private int numeroDeSocio;
    private String direccion;
    private LocalDate fechaDeNacimiento;





    private Biblioteca_Biblioteca biblioteca_biblioteca;


    public Biblioteca_Socio(
        int edad,        String nombreCompleto,        String telefono,        int numeroDeSocio,        String direccion,        LocalDate fechaDeNacimiento    ) {
        this.edad = edad;
        this.nombreCompleto = nombreCompleto;
        this.telefono = telefono;
        this.numeroDeSocio = numeroDeSocio;
        this.direccion = direccion;
        this.fechaDeNacimiento = fechaDeNacimiento;
    }


    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }
    public String getNombrecompleto() {
        return nombreCompleto;
    }

    public void setNombrecompleto(String nombreCompleto) {
        this.nombreCompleto = nombreCompleto;
    }
    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
    public int getNumerodesocio() {
        return numeroDeSocio;
    }

    public void setNumerodesocio(int numeroDeSocio) {
        this.numeroDeSocio = numeroDeSocio;
    }
    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    public LocalDate getFechadenacimiento() {
        return fechaDeNacimiento;
    }

    public void setFechadenacimiento(LocalDate fechaDeNacimiento) {
        this.fechaDeNacimiento = fechaDeNacimiento;
    }

    public Biblioteca_Biblioteca getBiblioteca_biblioteca() {
        return biblioteca_biblioteca;
    }

    public void setBiblioteca_biblioteca(Biblioteca_Biblioteca biblioteca_biblioteca) {
        this.biblioteca_biblioteca = biblioteca_biblioteca;
    }

}
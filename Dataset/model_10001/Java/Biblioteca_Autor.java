




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Biblioteca_Autor  {

    private String nombreCompleto;
    private String nacionalidad;
    private LocalDate fechaDeNacimiento;





    private Biblioteca_Biblioteca biblioteca_biblioteca;




    private List<Biblioteca_Libro> biblioteca_libros;




    private Biblioteca_Libro biblioteca_libro;


    public Biblioteca_Autor(
        String nombreCompleto,        String nacionalidad,        LocalDate fechaDeNacimiento    ) {
        this.nombreCompleto = nombreCompleto;
        this.nacionalidad = nacionalidad;
        this.fechaDeNacimiento = fechaDeNacimiento;
        this.biblioteca_libros = new ArrayList<>();
    }

    public Biblioteca_Autor(
        String nombreCompleto,        String nacionalidad,        LocalDate fechaDeNacimiento        ArrayList<Biblioteca_Libro> biblioteca_libros    ) {
        this.nombreCompleto = nombreCompleto;
        this.nacionalidad = nacionalidad;
        this.fechaDeNacimiento = fechaDeNacimiento;
        this.biblioteca_libros = biblioteca_libros;
    }

    public String getNombrecompleto() {
        return nombreCompleto;
    }

    public void setNombrecompleto(String nombreCompleto) {
        this.nombreCompleto = nombreCompleto;
    }
    public String getNacionalidad() {
        return nacionalidad;
    }

    public void setNacionalidad(String nacionalidad) {
        this.nacionalidad = nacionalidad;
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
    public List<Biblioteca_Libro> getBiblioteca_libros() {
        return biblioteca_libros;
    }

    public void addBiblioteca_libro(Biblioteca_libro biblioteca_libro) {
        this.biblioteca_libros.add(biblioteca_libro);
    }
    public Biblioteca_Libro getBiblioteca_libro() {
        return biblioteca_libro;
    }

    public void setBiblioteca_libro(Biblioteca_Libro biblioteca_libro) {
        this.biblioteca_libro = biblioteca_libro;
    }

}
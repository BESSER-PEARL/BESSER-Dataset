





import java.util.List;
import java.util.ArrayList;

public class Biblioteca_Libro  {

    private String ISBN;
    private boolean activo;
    private String titulo;
    private String genero;
    private String editorial;
    private int anioDeEdicion;





    private Biblioteca_Biblioteca biblioteca_biblioteca;


    public Biblioteca_Libro(
        String ISBN,        boolean activo,        String titulo,        String genero,        String editorial,        int anioDeEdicion    ) {
        this.ISBN = ISBN;
        this.activo = activo;
        this.titulo = titulo;
        this.genero = genero;
        this.editorial = editorial;
        this.anioDeEdicion = anioDeEdicion;
    }


    public String getIsbn() {
        return ISBN;
    }

    public void setIsbn(String ISBN) {
        this.ISBN = ISBN;
    }
    public boolean getActivo() {
        return activo;
    }

    public void setActivo(boolean activo) {
        this.activo = activo;
    }
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }
    public String getEditorial() {
        return editorial;
    }

    public void setEditorial(String editorial) {
        this.editorial = editorial;
    }
    public int getAniodeedicion() {
        return anioDeEdicion;
    }

    public void setAniodeedicion(int anioDeEdicion) {
        this.anioDeEdicion = anioDeEdicion;
    }

    public Biblioteca_Biblioteca getBiblioteca_biblioteca() {
        return biblioteca_biblioteca;
    }

    public void setBiblioteca_biblioteca(Biblioteca_Biblioteca biblioteca_biblioteca) {
        this.biblioteca_biblioteca = biblioteca_biblioteca;
    }

}
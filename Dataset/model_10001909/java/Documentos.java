





import java.util.List;
import java.util.ArrayList;

public class Documentos  {

    private String editorial;
    private String fechaCreaci_n;
    private String d_a;
    private String mesPublicaci_n;
    private String autores;
    private String fechaPublicaci_n;
    private String ISBN;
    private String titulo;



    public Documentos(
        String editorial,        String fechaCreaci_n,        String d_a,        String mesPublicaci_n,        String autores,        String fechaPublicaci_n,        String ISBN,        String titulo    ) {
        this.editorial = editorial;
        this.fechaCreaci_n = fechaCreaci_n;
        this.d_a = d_a;
        this.mesPublicaci_n = mesPublicaci_n;
        this.autores = autores;
        this.fechaPublicaci_n = fechaPublicaci_n;
        this.ISBN = ISBN;
        this.titulo = titulo;
    }


    public String getEditorial() {
        return editorial;
    }

    public void setEditorial(String editorial) {
        this.editorial = editorial;
    }
    public String getFechacreaci_n() {
        return fechaCreaci_n;
    }

    public void setFechacreaci_n(String fechaCreaci_n) {
        this.fechaCreaci_n = fechaCreaci_n;
    }
    public String getD_a() {
        return d_a;
    }

    public void setD_a(String d_a) {
        this.d_a = d_a;
    }
    public String getMespublicaci_n() {
        return mesPublicaci_n;
    }

    public void setMespublicaci_n(String mesPublicaci_n) {
        this.mesPublicaci_n = mesPublicaci_n;
    }
    public String getAutores() {
        return autores;
    }

    public void setAutores(String autores) {
        this.autores = autores;
    }
    public String getFechapublicaci_n() {
        return fechaPublicaci_n;
    }

    public void setFechapublicaci_n(String fechaPublicaci_n) {
        this.fechaPublicaci_n = fechaPublicaci_n;
    }
    public String getIsbn() {
        return ISBN;
    }

    public void setIsbn(String ISBN) {
        this.ISBN = ISBN;
    }
    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }


}
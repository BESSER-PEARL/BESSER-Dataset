





import java.util.List;
import java.util.ArrayList;

public class Buch  {

    private String ISBN;
    private String Autor;



    public Buch(
        String ISBN,        String Autor    ) {
        this.ISBN = ISBN;
        this.Autor = Autor;
    }


    public String getIsbn() {
        return ISBN;
    }

    public void setIsbn(String ISBN) {
        this.ISBN = ISBN;
    }
    public String getAutor() {
        return Autor;
    }

    public void setAutor(String Autor) {
        this.Autor = Autor;
    }


}
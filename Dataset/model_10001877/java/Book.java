





import java.util.List;
import java.util.ArrayList;

public class Book  {

    private String title;
    private int id;
    private String creation_date;
    private String status;
    private String author;





    private Librarian librarian;




    private Patron patron;


    public Book(
        String title,        int id,        String creation_date,        String status,        String author    ) {
        this.title = title;
        this.id = id;
        this.creation_date = creation_date;
        this.status = status;
        this.author = author;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCreation_date() {
        return creation_date;
    }

    public void setCreation_date(String creation_date) {
        this.creation_date = creation_date;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public Librarian getLibrarian() {
        return librarian;
    }

    public void setLibrarian(Librarian librarian) {
        this.librarian = librarian;
    }
    public Patron getPatron() {
        return patron;
    }

    public void setPatron(Patron patron) {
        this.patron = patron;
    }

}
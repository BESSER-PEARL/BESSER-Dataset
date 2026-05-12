





import java.util.List;
import java.util.ArrayList;

public class Patron  {

    private String position;
    private int id;
    private String name;





    private Magazine magazine;




    private Book book;


    public Patron(
        String position,        int id,        String name    ) {
        this.position = position;
        this.id = id;
        this.name = name;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Magazine getMagazine() {
        return magazine;
    }

    public void setMagazine(Magazine magazine) {
        this.magazine = magazine;
    }
    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Patron  {

    private String name;
    private String position;
    private int id;





    private Book book;




    private Magazine magazine;


    public Patron(
        String name,        String position,        int id    ) {
        this.name = name;
        this.position = position;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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

    public Book getBook() {
        return book;
    }

    public void setBook(Book book) {
        this.book = book;
    }
    public Magazine getMagazine() {
        return magazine;
    }

    public void setMagazine(Magazine magazine) {
        this.magazine = magazine;
    }

}
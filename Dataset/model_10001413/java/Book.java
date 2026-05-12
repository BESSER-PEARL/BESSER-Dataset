





import java.util.List;
import java.util.ArrayList;

public class Book  {

    private String description;
    private int bookID;
    private String author;
    private String title;
    private int price;
    private None category;





    private Administrator administrator;




    private Administrator administrator;


    public Book(
        String description,        int bookID,        String author,        String title,        int price,        None category    ) {
        this.description = description;
        this.bookID = bookID;
        this.author = author;
        this.title = title;
        this.price = price;
        this.category = category;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getBookid() {
        return bookID;
    }

    public void setBookid(int bookID) {
        this.bookID = bookID;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public None getCategory() {
        return category;
    }

    public void setCategory(None category) {
        this.category = category;
    }

    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }
    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }

}






import java.util.List;
import java.util.ArrayList;

public class books_Book  {

    private float price;
    private String year;
    private String author;





    private books_Bookstore books_bookstore;


    public books_Book(
        float price,        String year,        String author    ) {
        this.price = price;
        this.year = year;
        this.author = author;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public books_Bookstore getBooks_bookstore() {
        return books_bookstore;
    }

    public void setBooks_bookstore(books_Bookstore books_bookstore) {
        this.books_bookstore = books_bookstore;
    }

}
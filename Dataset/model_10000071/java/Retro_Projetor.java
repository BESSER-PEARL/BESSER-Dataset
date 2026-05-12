





import java.util.List;
import java.util.ArrayList;

public class Retro_Projetor  {

    private int book_qty;
    private String publisher;
    private int book_id;
    private String ISBN_no;
    private String author_name;
    private String title;



    public Retro_Projetor(
        int book_qty,        String publisher,        int book_id,        String ISBN_no,        String author_name,        String title    ) {
        this.book_qty = book_qty;
        this.publisher = publisher;
        this.book_id = book_id;
        this.ISBN_no = ISBN_no;
        this.author_name = author_name;
        this.title = title;
    }


    public int getBook_qty() {
        return book_qty;
    }

    public void setBook_qty(int book_qty) {
        this.book_qty = book_qty;
    }
    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public int getBook_id() {
        return book_id;
    }

    public void setBook_id(int book_id) {
        this.book_id = book_id;
    }
    public String getIsbn_no() {
        return ISBN_no;
    }

    public void setIsbn_no(String ISBN_no) {
        this.ISBN_no = ISBN_no;
    }
    public String getAuthor_name() {
        return author_name;
    }

    public void setAuthor_name(String author_name) {
        this.author_name = author_name;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}
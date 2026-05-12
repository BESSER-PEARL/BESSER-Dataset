





import java.util.List;
import java.util.ArrayList;

public class Books  {

    private String ISBN_no;
    private int book_qty;
    private String publisher;
    private String author_name;
    private int book_id;
    private String title;



    public Books(
        String ISBN_no,        int book_qty,        String publisher,        String author_name,        int book_id,        String title    ) {
        this.ISBN_no = ISBN_no;
        this.book_qty = book_qty;
        this.publisher = publisher;
        this.author_name = author_name;
        this.book_id = book_id;
        this.title = title;
    }


    public String getIsbn_no() {
        return ISBN_no;
    }

    public void setIsbn_no(String ISBN_no) {
        this.ISBN_no = ISBN_no;
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
    public String getAuthor_name() {
        return author_name;
    }

    public void setAuthor_name(String author_name) {
        this.author_name = author_name;
    }
    public int getBook_id() {
        return book_id;
    }

    public void setBook_id(int book_id) {
        this.book_id = book_id;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}
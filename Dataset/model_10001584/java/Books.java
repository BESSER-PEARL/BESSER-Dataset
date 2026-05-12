





import java.util.List;
import java.util.ArrayList;

public class Books  {

    private String author_name;
    private String ISBN_no;
    private int book_qty;
    private String title;
    private String publisher;
    private int book_id;



    public Books(
        String author_name,        String ISBN_no,        int book_qty,        String title,        String publisher,        int book_id    ) {
        this.author_name = author_name;
        this.ISBN_no = ISBN_no;
        this.book_qty = book_qty;
        this.title = title;
        this.publisher = publisher;
        this.book_id = book_id;
    }


    public String getAuthor_name() {
        return author_name;
    }

    public void setAuthor_name(String author_name) {
        this.author_name = author_name;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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


}
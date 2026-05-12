





import java.util.List;
import java.util.ArrayList;

public class book  {

    private int pages;
    private String title;
    private int ISBN;
    private String publisher;
    private String author;
    private String type;





    private loan_book loan_book;


    public book(
        int pages,        String title,        int ISBN,        String publisher,        String author,        String type    ) {
        this.pages = pages;
        this.title = title;
        this.ISBN = ISBN;
        this.publisher = publisher;
        this.author = author;
        this.type = type;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getIsbn() {
        return ISBN;
    }

    public void setIsbn(int ISBN) {
        this.ISBN = ISBN;
    }
    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public loan_book getLoan_book() {
        return loan_book;
    }

    public void setLoan_book(loan_book loan_book) {
        this.loan_book = loan_book;
    }

}
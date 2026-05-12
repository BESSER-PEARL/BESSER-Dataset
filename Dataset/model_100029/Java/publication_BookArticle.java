





import java.util.List;
import java.util.ArrayList;

public class publication_BookArticle extends Article {

    private String section;





    private List<publication_Book> publication_books;




    private publication_Book publication_book;


    public publication_BookArticle(
        String section    ) {
        super(
        );
        this.section = section;
        this.publication_books = new ArrayList<>();
    }

    public publication_BookArticle(
        String section        ArrayList<publication_Book> publication_books    ) {
        this.section = section;
        this.publication_books = publication_books;
    }

    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }

    public List<publication_Book> getPublication_books() {
        return publication_books;
    }

    public void addPublication_book(Publication_book publication_book) {
        this.publication_books.add(publication_book);
    }
    public publication_Book getPublication_book() {
        return publication_book;
    }

    public void setPublication_book(publication_Book publication_book) {
        this.publication_book = publication_book;
    }

}
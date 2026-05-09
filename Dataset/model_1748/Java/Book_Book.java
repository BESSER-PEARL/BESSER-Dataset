





import java.util.List;
import java.util.ArrayList;

public class Book_Book  {

    private String title;
    private int nbpages;
    private String isbn;





    private List<Book_Author> book_authors;




    private Book_Library book_library;




    private List<Book_Chapter> book_chapters;


    public Book_Book(
        String title,        int nbpages,        String isbn    ) {
        this.title = title;
        this.nbpages = nbpages;
        this.isbn = isbn;
        this.book_authors = new ArrayList<>();
        this.book_chapters = new ArrayList<>();
    }

    public Book_Book(
        String title,        int nbpages,        String isbn        ArrayList<Book_Author> book_authors,        ArrayList<Book_Chapter> book_chapters    ) {
        this.title = title;
        this.nbpages = nbpages;
        this.isbn = isbn;
        this.book_authors = book_authors;
        this.book_chapters = book_chapters;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getNbpages() {
        return nbpages;
    }

    public void setNbpages(int nbpages) {
        this.nbpages = nbpages;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public List<Book_Author> getBook_authors() {
        return book_authors;
    }

    public void addBook_author(Book_author book_author) {
        this.book_authors.add(book_author);
    }
    public Book_Library getBook_library() {
        return book_library;
    }

    public void setBook_library(Book_Library book_library) {
        this.book_library = book_library;
    }
    public List<Book_Chapter> getBook_chapters() {
        return book_chapters;
    }

    public void addBook_chapter(Book_chapter book_chapter) {
        this.book_chapters.add(book_chapter);
    }

}
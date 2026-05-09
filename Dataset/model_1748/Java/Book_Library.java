





import java.util.List;
import java.util.ArrayList;

public class Book_Library  {






    private List<Book_Author> book_authors;


    public Book_Library(
    ) {
        this.book_authors = new ArrayList<>();
    }

    public Book_Library(
        ArrayList<Book_Author> book_authors    ) {
        this.book_authors = book_authors;
    }


    public List<Book_Author> getBook_authors() {
        return book_authors;
    }

    public void addBook_author(Book_author book_author) {
        this.book_authors.add(book_author);
    }

}
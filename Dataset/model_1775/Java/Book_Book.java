





import java.util.List;
import java.util.ArrayList;

public class Book_Book  {

    private String title;





    private List<Book_Chapter> book_chapters;




    private Book_Chapter book_chapter;


    public Book_Book(
        String title    ) {
        this.title = title;
        this.book_chapters = new ArrayList<>();
    }

    public Book_Book(
        String title        ArrayList<Book_Chapter> book_chapters    ) {
        this.title = title;
        this.book_chapters = book_chapters;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<Book_Chapter> getBook_chapters() {
        return book_chapters;
    }

    public void addBook_chapter(Book_chapter book_chapter) {
        this.book_chapters.add(book_chapter);
    }
    public Book_Chapter getBook_chapter() {
        return book_chapter;
    }

    public void setBook_chapter(Book_Chapter book_chapter) {
        this.book_chapter = book_chapter;
    }

}
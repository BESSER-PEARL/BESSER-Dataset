





import java.util.List;
import java.util.ArrayList;

public class BOOKS_Book  {

    private String title;





    private List<BOOKS_Chapter> books_chapters;


    public BOOKS_Book(
        String title    ) {
        this.title = title;
        this.books_chapters = new ArrayList<>();
    }

    public BOOKS_Book(
        String title        ArrayList<BOOKS_Chapter> books_chapters    ) {
        this.title = title;
        this.books_chapters = books_chapters;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<BOOKS_Chapter> getBooks_chapters() {
        return books_chapters;
    }

    public void addBooks_chapter(Books_chapter books_chapter) {
        this.books_chapters.add(books_chapter);
    }

}
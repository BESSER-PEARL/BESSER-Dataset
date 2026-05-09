





import java.util.List;
import java.util.ArrayList;

public class tutorial_Library  {

    private String name;





    private List<tutorial_Book> tutorial_books;




    private tutorial_Book tutorial_book;


    public tutorial_Library(
        String name    ) {
        this.name = name;
        this.tutorial_books = new ArrayList<>();
    }

    public tutorial_Library(
        String name        ArrayList<tutorial_Book> tutorial_books    ) {
        this.name = name;
        this.tutorial_books = tutorial_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tutorial_Book> getTutorial_books() {
        return tutorial_books;
    }

    public void addTutorial_book(Tutorial_book tutorial_book) {
        this.tutorial_books.add(tutorial_book);
    }
    public tutorial_Book getTutorial_book() {
        return tutorial_book;
    }

    public void setTutorial_book(tutorial_Book tutorial_book) {
        this.tutorial_book = tutorial_book;
    }

}
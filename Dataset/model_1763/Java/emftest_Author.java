





import java.util.List;
import java.util.ArrayList;

public class emftest_Author  {

    private String name;





    private List<emftest_Book> emftest_books;




    private emftest_Book emftest_book;


    public emftest_Author(
        String name    ) {
        this.name = name;
        this.emftest_books = new ArrayList<>();
    }

    public emftest_Author(
        String name        ArrayList<emftest_Book> emftest_books    ) {
        this.name = name;
        this.emftest_books = emftest_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<emftest_Book> getEmftest_books() {
        return emftest_books;
    }

    public void addEmftest_book(Emftest_book emftest_book) {
        this.emftest_books.add(emftest_book);
    }
    public emftest_Book getEmftest_book() {
        return emftest_book;
    }

    public void setEmftest_book(emftest_Book emftest_book) {
        this.emftest_book = emftest_book;
    }

}
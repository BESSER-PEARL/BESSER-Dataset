





import java.util.List;
import java.util.ArrayList;

public class simpleanySimplified_Library  {






    private List<simpleanySimplified_Book> simpleanysimplified_books;


    public simpleanySimplified_Library(
    ) {
        this.simpleanysimplified_books = new ArrayList<>();
    }

    public simpleanySimplified_Library(
        ArrayList<simpleanySimplified_Book> simpleanysimplified_books    ) {
        this.simpleanysimplified_books = simpleanysimplified_books;
    }


    public List<simpleanySimplified_Book> getSimpleanysimplified_books() {
        return simpleanysimplified_books;
    }

    public void addSimpleanysimplified_book(Simpleanysimplified_book simpleanysimplified_book) {
        this.simpleanysimplified_books.add(simpleanysimplified_book);
    }

}
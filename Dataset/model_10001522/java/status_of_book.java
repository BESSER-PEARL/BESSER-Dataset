





import java.util.List;
import java.util.ArrayList;

public class status_of_book  {






    private List<library_member> library_members;




    private book book;


    public status_of_book(
    ) {
        this.library_members = new ArrayList<>();
    }

    public status_of_book(
        ArrayList<library_member> library_members    ) {
        this.library_members = library_members;
    }


    public List<library_member> getLibrary_members() {
        return library_members;
    }

    public void addLibrary_member(Library_member library_member) {
        this.library_members.add(library_member);
    }
    public book getBook() {
        return book;
    }

    public void setBook(book book) {
        this.book = book;
    }

}
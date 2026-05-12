





import java.util.List;
import java.util.ArrayList;

public class library_member  {






    private List<librarian> librarians;


    public library_member(
    ) {
        this.librarians = new ArrayList<>();
    }

    public library_member(
        ArrayList<librarian> librarians    ) {
        this.librarians = librarians;
    }


    public List<librarian> getLibrarians() {
        return librarians;
    }

    public void addLibrarian(Librarian librarian) {
        this.librarians.add(librarian);
    }

}
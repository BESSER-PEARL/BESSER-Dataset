





import java.util.List;
import java.util.ArrayList;

public class Library  {

    private int librarian_id;
    private int id;





    private Librarian librarian;




    private List<Patron> patrons;


    public Library(
        int librarian_id,        int id    ) {
        this.librarian_id = librarian_id;
        this.id = id;
        this.patrons = new ArrayList<>();
    }

    public Library(
        int librarian_id,        int id        ArrayList<Patron> patrons    ) {
        this.librarian_id = librarian_id;
        this.id = id;
        this.patrons = patrons;
    }

    public int getLibrarian_id() {
        return librarian_id;
    }

    public void setLibrarian_id(int librarian_id) {
        this.librarian_id = librarian_id;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Librarian getLibrarian() {
        return librarian;
    }

    public void setLibrarian(Librarian librarian) {
        this.librarian = librarian;
    }
    public List<Patron> getPatrons() {
        return patrons;
    }

    public void addPatron(Patron patron) {
        this.patrons.add(patron);
    }

}






import java.util.List;
import java.util.ArrayList;

public class Librarian  {

    private String name;
    private int id;





    private List<Patron> patrons;


    public Librarian(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
        this.patrons = new ArrayList<>();
    }

    public Librarian(
        String name,        int id        ArrayList<Patron> patrons    ) {
        this.name = name;
        this.id = id;
        this.patrons = patrons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Patron> getPatrons() {
        return patrons;
    }

    public void addPatron(Patron patron) {
        this.patrons.add(patron);
    }

}
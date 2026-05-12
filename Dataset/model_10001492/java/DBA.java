





import java.util.List;
import java.util.ArrayList;

public class DBA  {

    private int ID;
    private String name;
    private String email;





    private librarian librarian;


    public DBA(
        int ID,        String name,        String email    ) {
        this.ID = ID;
        this.name = name;
        this.email = email;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public librarian getLibrarian() {
        return librarian;
    }

    public void setLibrarian(librarian librarian) {
        this.librarian = librarian;
    }

}
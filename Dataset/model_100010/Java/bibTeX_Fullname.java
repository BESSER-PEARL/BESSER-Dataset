





import java.util.List;
import java.util.ArrayList;

public class bibTeX_Fullname  {

    private String lastname;
    private String firstname;





    private bibTeX_Authors bibtex_authors;


    public bibTeX_Fullname(
        String lastname,        String firstname    ) {
        this.lastname = lastname;
        this.firstname = firstname;
    }


    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public bibTeX_Authors getBibtex_authors() {
        return bibtex_authors;
    }

    public void setBibtex_authors(bibTeX_Authors bibtex_authors) {
        this.bibtex_authors = bibtex_authors;
    }

}
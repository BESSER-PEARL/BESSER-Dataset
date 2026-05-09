





import java.util.List;
import java.util.ArrayList;

public class library_Lend extends Command {

    private String firstname;
    private String isbn;
    private String secondname;



    public library_Lend(
        String firstname,        String isbn,        String secondname    ) {
        super(
        );
        this.firstname = firstname;
        this.isbn = isbn;
        this.secondname = secondname;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    public String getSecondname() {
        return secondname;
    }

    public void setSecondname(String secondname) {
        this.secondname = secondname;
    }


}
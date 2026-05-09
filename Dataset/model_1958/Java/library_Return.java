





import java.util.List;
import java.util.ArrayList;

public class library_Return extends Command {

    private String firstname;
    private String secondname;
    private String isbn;



    public library_Return(
        String firstname,        String secondname,        String isbn    ) {
        super(
        );
        this.firstname = firstname;
        this.secondname = secondname;
        this.isbn = isbn;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getSecondname() {
        return secondname;
    }

    public void setSecondname(String secondname) {
        this.secondname = secondname;
    }
    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }


}
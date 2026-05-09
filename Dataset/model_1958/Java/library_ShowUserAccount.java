





import java.util.List;
import java.util.ArrayList;

public class library_ShowUserAccount extends Command {

    private String firstname;
    private String secondname;



    public library_ShowUserAccount(
        String firstname,        String secondname    ) {
        super(
        );
        this.firstname = firstname;
        this.secondname = secondname;
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


}
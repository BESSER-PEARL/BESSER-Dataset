





import java.util.List;
import java.util.ArrayList;

public class Bursar  {

    private String firstname;
    private String lastname;



    public Bursar(
        String firstname,        String lastname    ) {
        this.firstname = firstname;
        this.lastname = lastname;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }


}






import java.util.List;
import java.util.ArrayList;

public class Families_Member  {

    private String firstname;
    private String gender;



    public Families_Member(
        String firstname,        String gender    ) {
        this.firstname = firstname;
        this.gender = gender;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }


}
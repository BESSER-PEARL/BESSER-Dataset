





import java.util.List;
import java.util.ArrayList;

public class VorkursModel_Person  {

    private String subject;
    private String lastname;
    private String firstname;
    private String gender;



    public VorkursModel_Person(
        String subject,        String lastname,        String firstname,        String gender    ) {
        this.subject = subject;
        this.lastname = lastname;
        this.firstname = firstname;
        this.gender = gender;
    }


    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
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
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }


}
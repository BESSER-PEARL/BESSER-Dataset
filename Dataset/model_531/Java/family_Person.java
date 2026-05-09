




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class family_Person  {

    private String lastname;
    private LocalDate birthdate;
    private String firstname;



    public family_Person(
        String lastname,        LocalDate birthdate,        String firstname    ) {
        this.lastname = lastname;
        this.birthdate = birthdate;
        this.firstname = firstname;
    }


    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public LocalDate getBirthdate() {
        return birthdate;
    }

    public void setBirthdate(LocalDate birthdate) {
        this.birthdate = birthdate;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }


}
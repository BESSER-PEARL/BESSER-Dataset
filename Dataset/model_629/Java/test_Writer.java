




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class test_Writer  {

    private LocalDate BirthDate;
    private String lastName;
    private String firstName;
    private String EMail;
    private boolean Pseudonym;



    public test_Writer(
        LocalDate BirthDate,        String lastName,        String firstName,        String EMail,        boolean Pseudonym    ) {
        this.BirthDate = BirthDate;
        this.lastName = lastName;
        this.firstName = firstName;
        this.EMail = EMail;
        this.Pseudonym = Pseudonym;
    }


    public LocalDate getBirthdate() {
        return BirthDate;
    }

    public void setBirthdate(LocalDate BirthDate) {
        this.BirthDate = BirthDate;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getEmail() {
        return EMail;
    }

    public void setEmail(String EMail) {
        this.EMail = EMail;
    }
    public boolean getPseudonym() {
        return Pseudonym;
    }

    public void setPseudonym(boolean Pseudonym) {
        this.Pseudonym = Pseudonym;
    }


}
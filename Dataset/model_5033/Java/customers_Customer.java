




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class customers_Customer  {

    private String comment;
    private LocalDate dateOfBirth;
    private String firstName;
    private String lastName;



    public customers_Customer(
        String comment,        LocalDate dateOfBirth,        String firstName,        String lastName    ) {
        this.comment = comment;
        this.dateOfBirth = dateOfBirth;
        this.firstName = firstName;
        this.lastName = lastName;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }


}
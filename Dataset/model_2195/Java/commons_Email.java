





import java.util.List;
import java.util.ArrayList;

public class commons_Email  {

    private String validationTime;
    private String email;
    private boolean primary;





    private commons_Person commons_person;


    public commons_Email(
        String validationTime,        String email,        boolean primary    ) {
        this.validationTime = validationTime;
        this.email = email;
        this.primary = primary;
    }


    public String getValidationtime() {
        return validationTime;
    }

    public void setValidationtime(String validationTime) {
        this.validationTime = validationTime;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public boolean getPrimary() {
        return primary;
    }

    public void setPrimary(boolean primary) {
        this.primary = primary;
    }

    public commons_Person getCommons_person() {
        return commons_person;
    }

    public void setCommons_person(commons_Person commons_person) {
        this.commons_person = commons_person;
    }

}
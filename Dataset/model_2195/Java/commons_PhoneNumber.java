





import java.util.List;
import java.util.ArrayList;

public class commons_PhoneNumber  {

    private String phoneNumber;
    private String validationTime;
    private boolean primary;





    private commons_Person commons_person;




    private commons_Person commons_person;


    public commons_PhoneNumber(
        String phoneNumber,        String validationTime,        boolean primary    ) {
        this.phoneNumber = phoneNumber;
        this.validationTime = validationTime;
        this.primary = primary;
    }


    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getValidationtime() {
        return validationTime;
    }

    public void setValidationtime(String validationTime) {
        this.validationTime = validationTime;
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
    public commons_Person getCommons_person() {
        return commons_person;
    }

    public void setCommons_person(commons_Person commons_person) {
        this.commons_person = commons_person;
    }

}






import java.util.List;
import java.util.ArrayList;

public class tda593_booking_Person extends LegalEntity {

    private String firstname;
    private String lastname;
    private String socialSecurityNumber;



    public tda593_booking_Person(
        String firstname,        String lastname,        String socialSecurityNumber    ) {
        super(
        );
        this.firstname = firstname;
        this.lastname = lastname;
        this.socialSecurityNumber = socialSecurityNumber;
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
    public String getSocialsecuritynumber() {
        return socialSecurityNumber;
    }

    public void setSocialsecuritynumber(String socialSecurityNumber) {
        this.socialSecurityNumber = socialSecurityNumber;
    }


}
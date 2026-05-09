





import java.util.List;
import java.util.ArrayList;

public class RootElement_Guest extends SupportTicketWriter, FeedbackWriter, MakeBooking {

    private String phoneNumber;
    private String name;
    private String nextDestination;
    private String nationality;
    private String mail;
    private String socialSecurityNumber;



    public RootElement_Guest(
        String phoneNumber,        String name,        String nextDestination,        String nationality,        String mail,        String socialSecurityNumber    ) {
        super(
        );
        this.phoneNumber = phoneNumber;
        this.name = name;
        this.nextDestination = nextDestination;
        this.nationality = nationality;
        this.mail = mail;
        this.socialSecurityNumber = socialSecurityNumber;
    }


    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNextdestination() {
        return nextDestination;
    }

    public void setNextdestination(String nextDestination) {
        this.nextDestination = nextDestination;
    }
    public String getNationality() {
        return nationality;
    }

    public void setNationality(String nationality) {
        this.nationality = nationality;
    }
    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }
    public String getSocialsecuritynumber() {
        return socialSecurityNumber;
    }

    public void setSocialsecuritynumber(String socialSecurityNumber) {
        this.socialSecurityNumber = socialSecurityNumber;
    }


}
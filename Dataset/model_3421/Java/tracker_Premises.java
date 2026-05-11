





import java.util.List;
import java.util.ArrayList;

public class tracker_Premises  {

    private String emailContact;
    private String premisesId;



    public tracker_Premises(
        String emailContact,        String premisesId    ) {
        this.emailContact = emailContact;
        this.premisesId = premisesId;
    }


    public String getEmailcontact() {
        return emailContact;
    }

    public void setEmailcontact(String emailContact) {
        this.emailContact = emailContact;
    }
    public String getPremisesid() {
        return premisesId;
    }

    public void setPremisesid(String premisesId) {
        this.premisesId = premisesId;
    }


}






import java.util.List;
import java.util.ArrayList;

public class commons_FacebookIdentity  {

    private String facebookUsername;
    private String facebookId;



    public commons_FacebookIdentity(
        String facebookUsername,        String facebookId    ) {
        this.facebookUsername = facebookUsername;
        this.facebookId = facebookId;
    }


    public String getFacebookusername() {
        return facebookUsername;
    }

    public void setFacebookusername(String facebookUsername) {
        this.facebookUsername = facebookUsername;
    }
    public String getFacebookid() {
        return facebookId;
    }

    public void setFacebookid(String facebookId) {
        this.facebookId = facebookId;
    }


}
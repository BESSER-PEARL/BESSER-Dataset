





import java.util.List;
import java.util.ArrayList;

public class SAFE_HOME_SYSTEM  {

    private String masterPwd;
    private String userId;
    private String streetAddress;
    private String activationState;



    public SAFE_HOME_SYSTEM(
        String masterPwd,        String userId,        String streetAddress,        String activationState    ) {
        this.masterPwd = masterPwd;
        this.userId = userId;
        this.streetAddress = streetAddress;
        this.activationState = activationState;
    }


    public String getMasterpwd() {
        return masterPwd;
    }

    public void setMasterpwd(String masterPwd) {
        this.masterPwd = masterPwd;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getStreetaddress() {
        return streetAddress;
    }

    public void setStreetaddress(String streetAddress) {
        this.streetAddress = streetAddress;
    }
    public String getActivationstate() {
        return activationState;
    }

    public void setActivationstate(String activationState) {
        this.activationState = activationState;
    }


}
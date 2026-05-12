





import java.util.List;
import java.util.ArrayList;

public class setup_GitCloneTask extends SetupTask {

    private String userID;
    private String checkoutBranch;
    private String pushURI;
    private String location;
    private String remoteName;
    private String remoteURI;



    public setup_GitCloneTask(
        String userID,        String checkoutBranch,        String pushURI,        String location,        String remoteName,        String remoteURI    ) {
        super(
        );
        this.userID = userID;
        this.checkoutBranch = checkoutBranch;
        this.pushURI = pushURI;
        this.location = location;
        this.remoteName = remoteName;
        this.remoteURI = remoteURI;
    }


    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getCheckoutbranch() {
        return checkoutBranch;
    }

    public void setCheckoutbranch(String checkoutBranch) {
        this.checkoutBranch = checkoutBranch;
    }
    public String getPushuri() {
        return pushURI;
    }

    public void setPushuri(String pushURI) {
        this.pushURI = pushURI;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getRemotename() {
        return remoteName;
    }

    public void setRemotename(String remoteName) {
        this.remoteName = remoteName;
    }
    public String getRemoteuri() {
        return remoteURI;
    }

    public void setRemoteuri(String remoteURI) {
        this.remoteURI = remoteURI;
    }


}
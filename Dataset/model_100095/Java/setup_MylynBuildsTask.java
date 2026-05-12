





import java.util.List;
import java.util.ArrayList;

public class setup_MylynBuildsTask extends SetupTask {

    private String userID;
    private String serverURL;
    private String connectorKind;
    private String password;



    public setup_MylynBuildsTask(
        String userID,        String serverURL,        String connectorKind,        String password    ) {
        super(
        );
        this.userID = userID;
        this.serverURL = serverURL;
        this.connectorKind = connectorKind;
        this.password = password;
    }


    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getServerurl() {
        return serverURL;
    }

    public void setServerurl(String serverURL) {
        this.serverURL = serverURL;
    }
    public String getConnectorkind() {
        return connectorKind;
    }

    public void setConnectorkind(String connectorKind) {
        this.connectorKind = connectorKind;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}
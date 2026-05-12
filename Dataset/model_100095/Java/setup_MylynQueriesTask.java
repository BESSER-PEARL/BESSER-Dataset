





import java.util.List;
import java.util.ArrayList;

public class setup_MylynQueriesTask extends SetupTask {

    private String password;
    private String userID;
    private String repositoryURL;
    private String connectorKind;



    public setup_MylynQueriesTask(
        String password,        String userID,        String repositoryURL,        String connectorKind    ) {
        super(
        );
        this.password = password;
        this.userID = userID;
        this.repositoryURL = repositoryURL;
        this.connectorKind = connectorKind;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getRepositoryurl() {
        return repositoryURL;
    }

    public void setRepositoryurl(String repositoryURL) {
        this.repositoryURL = repositoryURL;
    }
    public String getConnectorkind() {
        return connectorKind;
    }

    public void setConnectorkind(String connectorKind) {
        this.connectorKind = connectorKind;
    }


}
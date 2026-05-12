





import java.util.List;
import java.util.ArrayList;

public class builds_BuildServer extends BuildElement {

    private String location;
    private String connectorKind;
    private String repositoryUrl;



    public builds_BuildServer(
        String location,        String connectorKind,        String repositoryUrl    ) {
        super(
        );
        this.location = location;
        this.connectorKind = connectorKind;
        this.repositoryUrl = repositoryUrl;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getConnectorkind() {
        return connectorKind;
    }

    public void setConnectorkind(String connectorKind) {
        this.connectorKind = connectorKind;
    }
    public String getRepositoryurl() {
        return repositoryUrl;
    }

    public void setRepositoryurl(String repositoryUrl) {
        this.repositoryUrl = repositoryUrl;
    }


}
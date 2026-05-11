





import java.util.List;
import java.util.ArrayList;

public class builds_BuildServer extends BuildElement {

    private String connectorKind;
    private String location;
    private String repositoryUrl;



    public builds_BuildServer(
        String connectorKind,        String location,        String repositoryUrl    ) {
        super(
        );
        this.connectorKind = connectorKind;
        this.location = location;
        this.repositoryUrl = repositoryUrl;
    }


    public String getConnectorkind() {
        return connectorKind;
    }

    public void setConnectorkind(String connectorKind) {
        this.connectorKind = connectorKind;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getRepositoryurl() {
        return repositoryUrl;
    }

    public void setRepositoryurl(String repositoryUrl) {
        this.repositoryUrl = repositoryUrl;
    }


}
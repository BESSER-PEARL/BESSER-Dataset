





import java.util.List;
import java.util.ArrayList;

public class setup_MylynQueryTask extends SetupTask {

    private String connectorKind;
    private String repositoryURL;
    private String summary;
    private String relativeURL;



    public setup_MylynQueryTask(
        String connectorKind,        String repositoryURL,        String summary,        String relativeURL    ) {
        super(
        );
        this.connectorKind = connectorKind;
        this.repositoryURL = repositoryURL;
        this.summary = summary;
        this.relativeURL = relativeURL;
    }


    public String getConnectorkind() {
        return connectorKind;
    }

    public void setConnectorkind(String connectorKind) {
        this.connectorKind = connectorKind;
    }
    public String getRepositoryurl() {
        return repositoryURL;
    }

    public void setRepositoryurl(String repositoryURL) {
        this.repositoryURL = repositoryURL;
    }
    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }
    public String getRelativeurl() {
        return relativeURL;
    }

    public void setRelativeurl(String relativeURL) {
        this.relativeURL = relativeURL;
    }


}
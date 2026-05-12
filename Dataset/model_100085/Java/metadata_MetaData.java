





import java.util.List;
import java.util.ArrayList;

public class metadata_MetaData  {

    private String groupId;
    private String artifactId;
    private String version;





    private metadata_DocumentRoot metadata_documentroot;


    public metadata_MetaData(
        String groupId,        String artifactId,        String version    ) {
        this.groupId = groupId;
        this.artifactId = artifactId;
        this.version = version;
    }


    public String getGroupid() {
        return groupId;
    }

    public void setGroupid(String groupId) {
        this.groupId = groupId;
    }
    public String getArtifactid() {
        return artifactId;
    }

    public void setArtifactid(String artifactId) {
        this.artifactId = artifactId;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public metadata_DocumentRoot getMetadata_documentroot() {
        return metadata_documentroot;
    }

    public void setMetadata_documentroot(metadata_DocumentRoot metadata_documentroot) {
        this.metadata_documentroot = metadata_documentroot;
    }

}
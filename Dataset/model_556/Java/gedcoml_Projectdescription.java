





import java.util.List;
import java.util.ArrayList;

public class gedcoml_Projectdescription  {

    private String groupId;
    private String version;
    private String artifactId;
    private String publishingDate;



    public gedcoml_Projectdescription(
        String groupId,        String version,        String artifactId,        String publishingDate    ) {
        this.groupId = groupId;
        this.version = version;
        this.artifactId = artifactId;
        this.publishingDate = publishingDate;
    }


    public String getGroupid() {
        return groupId;
    }

    public void setGroupid(String groupId) {
        this.groupId = groupId;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getArtifactid() {
        return artifactId;
    }

    public void setArtifactid(String artifactId) {
        this.artifactId = artifactId;
    }
    public String getPublishingdate() {
        return publishingDate;
    }

    public void setPublishingdate(String publishingDate) {
        this.publishingDate = publishingDate;
    }


}
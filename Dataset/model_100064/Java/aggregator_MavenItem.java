





import java.util.List;
import java.util.ArrayList;

public class aggregator_MavenItem  {

    private String artifactId;
    private String groupId;



    public aggregator_MavenItem(
        String artifactId,        String groupId    ) {
        this.artifactId = artifactId;
        this.groupId = groupId;
    }


    public String getArtifactid() {
        return artifactId;
    }

    public void setArtifactid(String artifactId) {
        this.artifactId = artifactId;
    }
    public String getGroupid() {
        return groupId;
    }

    public void setGroupid(String groupId) {
        this.groupId = groupId;
    }


}
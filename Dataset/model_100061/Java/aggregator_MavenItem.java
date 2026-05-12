





import java.util.List;
import java.util.ArrayList;

public class aggregator_MavenItem  {

    private String groupId;
    private String artifactId;



    public aggregator_MavenItem(
        String groupId,        String artifactId    ) {
        this.groupId = groupId;
        this.artifactId = artifactId;
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


}
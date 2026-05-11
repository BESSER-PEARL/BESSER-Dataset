





import java.util.List;
import java.util.ArrayList;

public class aggregator_MavenItem  {

    private String artifactId;
    private String classifier;
    private String mappedVersion;
    private String groupId;





    private aggregator_MavenMapping aggregator_mavenmapping;


    public aggregator_MavenItem(
        String artifactId,        String classifier,        String mappedVersion,        String groupId    ) {
        this.artifactId = artifactId;
        this.classifier = classifier;
        this.mappedVersion = mappedVersion;
        this.groupId = groupId;
    }


    public String getArtifactid() {
        return artifactId;
    }

    public void setArtifactid(String artifactId) {
        this.artifactId = artifactId;
    }
    public String getClassifier() {
        return classifier;
    }

    public void setClassifier(String classifier) {
        this.classifier = classifier;
    }
    public String getMappedversion() {
        return mappedVersion;
    }

    public void setMappedversion(String mappedVersion) {
        this.mappedVersion = mappedVersion;
    }
    public String getGroupid() {
        return groupId;
    }

    public void setGroupid(String groupId) {
        this.groupId = groupId;
    }

    public aggregator_MavenMapping getAggregator_mavenmapping() {
        return aggregator_mavenmapping;
    }

    public void setAggregator_mavenmapping(aggregator_MavenMapping aggregator_mavenmapping) {
        this.aggregator_mavenmapping = aggregator_mavenmapping;
    }

}






import java.util.List;
import java.util.ArrayList;

public class aggregator_MavenMapping extends InfosProvider, StatusProvider {

    private String versionPattern;
    private String artifactId;
    private String namePattern;
    private String versionTemplate;
    private String groupId;





    private aggregator_Contribution aggregator_contribution;




    private aggregator_Aggregation aggregator_aggregation;


    public aggregator_MavenMapping(
        String versionPattern,        String artifactId,        String namePattern,        String versionTemplate,        String groupId    ) {
        super(
        );
        this.versionPattern = versionPattern;
        this.artifactId = artifactId;
        this.namePattern = namePattern;
        this.versionTemplate = versionTemplate;
        this.groupId = groupId;
    }


    public String getVersionpattern() {
        return versionPattern;
    }

    public void setVersionpattern(String versionPattern) {
        this.versionPattern = versionPattern;
    }
    public String getArtifactid() {
        return artifactId;
    }

    public void setArtifactid(String artifactId) {
        this.artifactId = artifactId;
    }
    public String getNamepattern() {
        return namePattern;
    }

    public void setNamepattern(String namePattern) {
        this.namePattern = namePattern;
    }
    public String getVersiontemplate() {
        return versionTemplate;
    }

    public void setVersiontemplate(String versionTemplate) {
        this.versionTemplate = versionTemplate;
    }
    public String getGroupid() {
        return groupId;
    }

    public void setGroupid(String groupId) {
        this.groupId = groupId;
    }

    public aggregator_Contribution getAggregator_contribution() {
        return aggregator_contribution;
    }

    public void setAggregator_contribution(aggregator_Contribution aggregator_contribution) {
        this.aggregator_contribution = aggregator_contribution;
    }
    public aggregator_Aggregation getAggregator_aggregation() {
        return aggregator_aggregation;
    }

    public void setAggregator_aggregation(aggregator_Aggregation aggregator_aggregation) {
        this.aggregator_aggregation = aggregator_aggregation;
    }

}
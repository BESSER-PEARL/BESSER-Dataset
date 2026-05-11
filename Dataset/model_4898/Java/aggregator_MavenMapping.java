





import java.util.List;
import java.util.ArrayList;

public class aggregator_MavenMapping extends StatusProvider, InfosProvider {

    private String namePattern;
    private String artifactId;
    private String groupId;





    private aggregator_Contribution aggregator_contribution;


    public aggregator_MavenMapping(
        String namePattern,        String artifactId,        String groupId    ) {
        super(
        );
        this.namePattern = namePattern;
        this.artifactId = artifactId;
        this.groupId = groupId;
    }


    public String getNamepattern() {
        return namePattern;
    }

    public void setNamepattern(String namePattern) {
        this.namePattern = namePattern;
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

    public aggregator_Contribution getAggregator_contribution() {
        return aggregator_contribution;
    }

    public void setAggregator_contribution(aggregator_Contribution aggregator_contribution) {
        this.aggregator_contribution = aggregator_contribution;
    }

}
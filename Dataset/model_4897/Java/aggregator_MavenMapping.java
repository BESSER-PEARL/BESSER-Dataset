





import java.util.List;
import java.util.ArrayList;

public class aggregator_MavenMapping extends StatusProvider, InfosProvider {

    private String artifactId;
    private String namePattern;
    private String groupId;





    private aggregator_Aggregation aggregator_aggregation;




    private aggregator_Contribution aggregator_contribution;


    public aggregator_MavenMapping(
        String artifactId,        String namePattern,        String groupId    ) {
        super(
        );
        this.artifactId = artifactId;
        this.namePattern = namePattern;
        this.groupId = groupId;
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
    public String getGroupid() {
        return groupId;
    }

    public void setGroupid(String groupId) {
        this.groupId = groupId;
    }

    public aggregator_Aggregation getAggregator_aggregation() {
        return aggregator_aggregation;
    }

    public void setAggregator_aggregation(aggregator_Aggregation aggregator_aggregation) {
        this.aggregator_aggregation = aggregator_aggregation;
    }
    public aggregator_Contribution getAggregator_contribution() {
        return aggregator_contribution;
    }

    public void setAggregator_contribution(aggregator_Contribution aggregator_contribution) {
        this.aggregator_contribution = aggregator_contribution;
    }

}
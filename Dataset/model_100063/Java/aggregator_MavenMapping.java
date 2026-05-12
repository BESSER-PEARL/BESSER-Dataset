





import java.util.List;
import java.util.ArrayList;

public class aggregator_MavenMapping extends InfosProvider, StatusProvider {

    private String groupId;
    private String namePattern;
    private String artifactId;





    private aggregator_Aggregator aggregator_aggregator;




    private aggregator_Contribution aggregator_contribution;


    public aggregator_MavenMapping(
        String groupId,        String namePattern,        String artifactId    ) {
        super(
        );
        this.groupId = groupId;
        this.namePattern = namePattern;
        this.artifactId = artifactId;
    }


    public String getGroupid() {
        return groupId;
    }

    public void setGroupid(String groupId) {
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

    public aggregator_Aggregator getAggregator_aggregator() {
        return aggregator_aggregator;
    }

    public void setAggregator_aggregator(aggregator_Aggregator aggregator_aggregator) {
        this.aggregator_aggregator = aggregator_aggregator;
    }
    public aggregator_Contribution getAggregator_contribution() {
        return aggregator_contribution;
    }

    public void setAggregator_contribution(aggregator_Contribution aggregator_contribution) {
        this.aggregator_contribution = aggregator_contribution;
    }

}
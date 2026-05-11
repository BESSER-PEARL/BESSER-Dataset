





import java.util.List;
import java.util.ArrayList;

public class aggregator_MappedRepository extends DescriptionProvider, IdentificationProvider, MetadataRepositoryReference {

    private boolean mirrorArtifacts;
    private String categoryPrefix;





    private List<aggregator_MapRule> aggregator_maprules;




    private aggregator_Contribution aggregator_contribution;


    public aggregator_MappedRepository(
        boolean mirrorArtifacts,        String categoryPrefix    ) {
        super(
        );
        this.mirrorArtifacts = mirrorArtifacts;
        this.categoryPrefix = categoryPrefix;
        this.aggregator_maprules = new ArrayList<>();
    }

    public aggregator_MappedRepository(
        boolean mirrorArtifacts,        String categoryPrefix        ArrayList<aggregator_MapRule> aggregator_maprules    ) {
        this.mirrorArtifacts = mirrorArtifacts;
        this.categoryPrefix = categoryPrefix;
        this.aggregator_maprules = aggregator_maprules;
    }

    public boolean getMirrorartifacts() {
        return mirrorArtifacts;
    }

    public void setMirrorartifacts(boolean mirrorArtifacts) {
        this.mirrorArtifacts = mirrorArtifacts;
    }
    public String getCategoryprefix() {
        return categoryPrefix;
    }

    public void setCategoryprefix(String categoryPrefix) {
        this.categoryPrefix = categoryPrefix;
    }

    public List<aggregator_MapRule> getAggregator_maprules() {
        return aggregator_maprules;
    }

    public void addAggregator_maprule(Aggregator_maprule aggregator_maprule) {
        this.aggregator_maprules.add(aggregator_maprule);
    }
    public aggregator_Contribution getAggregator_contribution() {
        return aggregator_contribution;
    }

    public void setAggregator_contribution(aggregator_Contribution aggregator_contribution) {
        this.aggregator_contribution = aggregator_contribution;
    }

}
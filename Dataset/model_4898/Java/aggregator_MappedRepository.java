





import java.util.List;
import java.util.ArrayList;

public class aggregator_MappedRepository extends DescriptionProvider, MetadataRepositoryReference, IdentificationProvider {

    private String categoryPrefix;
    private boolean mirrorArtifacts;





    private aggregator_Contribution aggregator_contribution;


    public aggregator_MappedRepository(
        String categoryPrefix,        boolean mirrorArtifacts    ) {
        super(
        );
        this.categoryPrefix = categoryPrefix;
        this.mirrorArtifacts = mirrorArtifacts;
    }


    public String getCategoryprefix() {
        return categoryPrefix;
    }

    public void setCategoryprefix(String categoryPrefix) {
        this.categoryPrefix = categoryPrefix;
    }
    public boolean getMirrorartifacts() {
        return mirrorArtifacts;
    }

    public void setMirrorartifacts(boolean mirrorArtifacts) {
        this.mirrorArtifacts = mirrorArtifacts;
    }

    public aggregator_Contribution getAggregator_contribution() {
        return aggregator_contribution;
    }

    public void setAggregator_contribution(aggregator_Contribution aggregator_contribution) {
        this.aggregator_contribution = aggregator_contribution;
    }

}
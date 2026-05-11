





import java.util.List;
import java.util.ArrayList;

public class aggregator_MappedRepository extends DescriptionProvider, IdentificationProvider, MetadataRepositoryReference {

    private String categoryPrefix;
    private boolean mirrorArtifacts;



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


}
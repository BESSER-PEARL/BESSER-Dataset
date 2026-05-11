





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification extends Identifier {

    private float failureProbability;





    private LinkingResource linkingresource;


    public pcm_pc_pc_resourceenvironment_pc_pc_CommunicationLinkResourceSpecification(
        float failureProbability    ) {
        super(
        );
        this.failureProbability = failureProbability;
    }


    public float getFailureprobability() {
        return failureProbability;
    }

    public void setFailureprobability(float failureProbability) {
        this.failureProbability = failureProbability;
    }

    public LinkingResource getLinkingresource() {
        return linkingresource;
    }

    public void setLinkingresource(LinkingResource linkingresource) {
        this.linkingresource = linkingresource;
    }

}
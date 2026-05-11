





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification extends Identifier {

    private float failureProbability;





    private CommunicationLinkResourceType communicationlinkresourcetype;


    public pcm_av_pc_resourceenvironment_av_pc_CommunicationLinkResourceSpecification(
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

    public CommunicationLinkResourceType getCommunicationlinkresourcetype() {
        return communicationlinkresourcetype;
    }

    public void setCommunicationlinkresourcetype(CommunicationLinkResourceType communicationlinkresourcetype) {
        this.communicationlinkresourcetype = communicationlinkresourcetype;
    }

}






import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Interaction_SwMutualExclusionResource extends GRM_MutualExclusionResource, SW_Interaction_SwSynchronizationResource {

    private String mechanism;
    private String concurrentAccessProtocol;



    public MARTE_SW_Interaction_SwMutualExclusionResource(
        String mechanism,        String concurrentAccessProtocol    ) {
        super(
        );
        this.mechanism = mechanism;
        this.concurrentAccessProtocol = concurrentAccessProtocol;
    }


    public String getMechanism() {
        return mechanism;
    }

    public void setMechanism(String mechanism) {
        this.mechanism = mechanism;
    }
    public String getConcurrentaccessprotocol() {
        return concurrentAccessProtocol;
    }

    public void setConcurrentaccessprotocol(String concurrentAccessProtocol) {
        this.concurrentAccessProtocol = concurrentAccessProtocol;
    }


}
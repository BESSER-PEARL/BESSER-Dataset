





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Interaction_SwMutualExclusionResource extends GRM_MutualExclusionResource, SW_Interaction_SwSynchronizationResource {

    private String concurrentAccessProtocol;
    private String mechanism;





    private List<SW_Interaction_MARTE_TypedElement> sw_interaction_marte_typedelements;


    public MARTE_SW_Interaction_SwMutualExclusionResource(
        String concurrentAccessProtocol,        String mechanism    ) {
        super(
        );
        this.concurrentAccessProtocol = concurrentAccessProtocol;
        this.mechanism = mechanism;
        this.sw_interaction_marte_typedelements = new ArrayList<>();
    }

    public MARTE_SW_Interaction_SwMutualExclusionResource(
        String concurrentAccessProtocol,        String mechanism        ArrayList<SW_Interaction_MARTE_TypedElement> sw_interaction_marte_typedelements    ) {
        this.concurrentAccessProtocol = concurrentAccessProtocol;
        this.mechanism = mechanism;
        this.sw_interaction_marte_typedelements = sw_interaction_marte_typedelements;
    }

    public String getConcurrentaccessprotocol() {
        return concurrentAccessProtocol;
    }

    public void setConcurrentaccessprotocol(String concurrentAccessProtocol) {
        this.concurrentAccessProtocol = concurrentAccessProtocol;
    }
    public String getMechanism() {
        return mechanism;
    }

    public void setMechanism(String mechanism) {
        this.mechanism = mechanism;
    }

    public List<SW_Interaction_MARTE_TypedElement> getSw_interaction_marte_typedelements() {
        return sw_interaction_marte_typedelements;
    }

    public void addSw_interaction_marte_typedelement(Sw_interaction_marte_typedelement sw_interaction_marte_typedelement) {
        this.sw_interaction_marte_typedelements.add(sw_interaction_marte_typedelement);
    }

}
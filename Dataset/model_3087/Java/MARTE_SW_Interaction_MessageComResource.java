





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Interaction_MessageComResource extends SwCommunicationResource {

    private String messageQueuePolicy;
    private String mechanism;
    private String isFixedMessageSize;





    private List<SW_Interaction_MARTE_TypedElement> sw_interaction_marte_typedelements;




    private List<SW_Interaction_MARTE_TypedElement> sw_interaction_marte_typedelements;


    public MARTE_SW_Interaction_MessageComResource(
        String messageQueuePolicy,        String mechanism,        String isFixedMessageSize    ) {
        super(
        );
        this.messageQueuePolicy = messageQueuePolicy;
        this.mechanism = mechanism;
        this.isFixedMessageSize = isFixedMessageSize;
        this.sw_interaction_marte_typedelements = new ArrayList<>();
        this.sw_interaction_marte_typedelements = new ArrayList<>();
    }

    public MARTE_SW_Interaction_MessageComResource(
        String messageQueuePolicy,        String mechanism,        String isFixedMessageSize        ArrayList<SW_Interaction_MARTE_TypedElement> sw_interaction_marte_typedelements,        ArrayList<SW_Interaction_MARTE_TypedElement> sw_interaction_marte_typedelements    ) {
        this.messageQueuePolicy = messageQueuePolicy;
        this.mechanism = mechanism;
        this.isFixedMessageSize = isFixedMessageSize;
        this.sw_interaction_marte_typedelements = sw_interaction_marte_typedelements;
        this.sw_interaction_marte_typedelements = sw_interaction_marte_typedelements;
    }

    public String getMessagequeuepolicy() {
        return messageQueuePolicy;
    }

    public void setMessagequeuepolicy(String messageQueuePolicy) {
        this.messageQueuePolicy = messageQueuePolicy;
    }
    public String getMechanism() {
        return mechanism;
    }

    public void setMechanism(String mechanism) {
        this.mechanism = mechanism;
    }
    public String getIsfixedmessagesize() {
        return isFixedMessageSize;
    }

    public void setIsfixedmessagesize(String isFixedMessageSize) {
        this.isFixedMessageSize = isFixedMessageSize;
    }

    public List<SW_Interaction_MARTE_TypedElement> getSw_interaction_marte_typedelements() {
        return sw_interaction_marte_typedelements;
    }

    public void addSw_interaction_marte_typedelement(Sw_interaction_marte_typedelement sw_interaction_marte_typedelement) {
        this.sw_interaction_marte_typedelements.add(sw_interaction_marte_typedelement);
    }
    public List<SW_Interaction_MARTE_TypedElement> getSw_interaction_marte_typedelements() {
        return sw_interaction_marte_typedelements;
    }

    public void addSw_interaction_marte_typedelement(Sw_interaction_marte_typedelement sw_interaction_marte_typedelement) {
        this.sw_interaction_marte_typedelements.add(sw_interaction_marte_typedelement);
    }

}
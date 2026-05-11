





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ConversationNode extends InteractionNode, BaseElement {

    private String name;





    private List<bpmn2_CorrelationKey> bpmn2_correlationkeys;


    public bpmn2_ConversationNode(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_correlationkeys = new ArrayList<>();
    }

    public bpmn2_ConversationNode(
        String name        ArrayList<bpmn2_CorrelationKey> bpmn2_correlationkeys    ) {
        this.name = name;
        this.bpmn2_correlationkeys = bpmn2_correlationkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<bpmn2_CorrelationKey> getBpmn2_correlationkeys() {
        return bpmn2_correlationkeys;
    }

    public void addBpmn2_correlationkey(Bpmn2_correlationkey bpmn2_correlationkey) {
        this.bpmn2_correlationkeys.add(bpmn2_correlationkey);
    }

}
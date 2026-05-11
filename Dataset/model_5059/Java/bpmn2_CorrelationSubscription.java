





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CorrelationSubscription extends BaseElement {






    private List<bpmn2_CorrelationPropertyBinding> bpmn2_correlationpropertybindings;


    public bpmn2_CorrelationSubscription(
    ) {
        super(
        );
        this.bpmn2_correlationpropertybindings = new ArrayList<>();
    }

    public bpmn2_CorrelationSubscription(
        ArrayList<bpmn2_CorrelationPropertyBinding> bpmn2_correlationpropertybindings    ) {
        this.bpmn2_correlationpropertybindings = bpmn2_correlationpropertybindings;
    }


    public List<bpmn2_CorrelationPropertyBinding> getBpmn2_correlationpropertybindings() {
        return bpmn2_correlationpropertybindings;
    }

    public void addBpmn2_correlationpropertybinding(Bpmn2_correlationpropertybinding bpmn2_correlationpropertybinding) {
        this.bpmn2_correlationpropertybindings.add(bpmn2_correlationpropertybinding);
    }

}
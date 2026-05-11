





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_CorrelationSubscription extends BaseElement {






    private List<BPMNProfile_CorrelationPropertyBinding> bpmnprofile_correlationpropertybindings;


    public BPMNProfile_CorrelationSubscription(
    ) {
        super(
        );
        this.bpmnprofile_correlationpropertybindings = new ArrayList<>();
    }

    public BPMNProfile_CorrelationSubscription(
        ArrayList<BPMNProfile_CorrelationPropertyBinding> bpmnprofile_correlationpropertybindings    ) {
        this.bpmnprofile_correlationpropertybindings = bpmnprofile_correlationpropertybindings;
    }


    public List<BPMNProfile_CorrelationPropertyBinding> getBpmnprofile_correlationpropertybindings() {
        return bpmnprofile_correlationpropertybindings;
    }

    public void addBpmnprofile_correlationpropertybinding(Bpmnprofile_correlationpropertybinding bpmnprofile_correlationpropertybinding) {
        this.bpmnprofile_correlationpropertybindings.add(bpmnprofile_correlationpropertybinding);
    }

}
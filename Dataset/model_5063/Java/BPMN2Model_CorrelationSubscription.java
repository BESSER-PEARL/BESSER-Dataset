





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_CorrelationSubscription extends BaseElement {






    private List<BPMN2Model_CorrelationPropertyBinding> bpmn2model_correlationpropertybindings;




    private BPMN2Model_Process bpmn2model_process;


    public BPMN2Model_CorrelationSubscription(
    ) {
        super(
        );
        this.bpmn2model_correlationpropertybindings = new ArrayList<>();
    }

    public BPMN2Model_CorrelationSubscription(
        ArrayList<BPMN2Model_CorrelationPropertyBinding> bpmn2model_correlationpropertybindings    ) {
        this.bpmn2model_correlationpropertybindings = bpmn2model_correlationpropertybindings;
    }


    public List<BPMN2Model_CorrelationPropertyBinding> getBpmn2model_correlationpropertybindings() {
        return bpmn2model_correlationpropertybindings;
    }

    public void addBpmn2model_correlationpropertybinding(Bpmn2model_correlationpropertybinding bpmn2model_correlationpropertybinding) {
        this.bpmn2model_correlationpropertybindings.add(bpmn2model_correlationpropertybinding);
    }
    public BPMN2Model_Process getBpmn2model_process() {
        return bpmn2model_process;
    }

    public void setBpmn2model_process(BPMN2Model_Process bpmn2model_process) {
        this.bpmn2model_process = bpmn2model_process;
    }

}
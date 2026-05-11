





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CorrelationSubscription extends BaseElement {






    private List<bpmn2_CorrelationPropertyBinding> bpmn2_correlationpropertybindings;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_CorrelationKey bpmn2_correlationkey;


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
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_CorrelationKey getBpmn2_correlationkey() {
        return bpmn2_correlationkey;
    }

    public void setBpmn2_correlationkey(bpmn2_CorrelationKey bpmn2_correlationkey) {
        this.bpmn2_correlationkey = bpmn2_correlationkey;
    }

}
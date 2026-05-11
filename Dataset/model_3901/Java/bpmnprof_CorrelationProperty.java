





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_CorrelationProperty extends BaseElement {






    private List<bpmnprof_CorrelationPropertyRetrievalExpression> bpmnprof_correlationpropertyretrievalexpressions;




    private bpmnprof_CorrelationKey bpmnprof_correlationkey;




    private bpmnprof_CorrelationPropertyBinding bpmnprof_correlationpropertybinding;


    public bpmnprof_CorrelationProperty(
    ) {
        super(
        );
        this.bpmnprof_correlationpropertyretrievalexpressions = new ArrayList<>();
    }

    public bpmnprof_CorrelationProperty(
        ArrayList<bpmnprof_CorrelationPropertyRetrievalExpression> bpmnprof_correlationpropertyretrievalexpressions    ) {
        this.bpmnprof_correlationpropertyretrievalexpressions = bpmnprof_correlationpropertyretrievalexpressions;
    }


    public List<bpmnprof_CorrelationPropertyRetrievalExpression> getBpmnprof_correlationpropertyretrievalexpressions() {
        return bpmnprof_correlationpropertyretrievalexpressions;
    }

    public void addBpmnprof_correlationpropertyretrievalexpression(Bpmnprof_correlationpropertyretrievalexpression bpmnprof_correlationpropertyretrievalexpression) {
        this.bpmnprof_correlationpropertyretrievalexpressions.add(bpmnprof_correlationpropertyretrievalexpression);
    }
    public bpmnprof_CorrelationKey getBpmnprof_correlationkey() {
        return bpmnprof_correlationkey;
    }

    public void setBpmnprof_correlationkey(bpmnprof_CorrelationKey bpmnprof_correlationkey) {
        this.bpmnprof_correlationkey = bpmnprof_correlationkey;
    }
    public bpmnprof_CorrelationPropertyBinding getBpmnprof_correlationpropertybinding() {
        return bpmnprof_correlationpropertybinding;
    }

    public void setBpmnprof_correlationpropertybinding(bpmnprof_CorrelationPropertyBinding bpmnprof_correlationpropertybinding) {
        this.bpmnprof_correlationpropertybinding = bpmnprof_correlationpropertybinding;
    }

}
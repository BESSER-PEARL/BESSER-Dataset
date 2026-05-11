





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Message extends RootElement {

    private String name;





    private bpmn2_CorrelationPropertyRetrievalExpression bpmn2_correlationpropertyretrievalexpression;




    private bpmn2_MessageFlow bpmn2_messageflow;




    private bpmn2_Operation bpmn2_operation;




    private bpmn2_Operation bpmn2_operation;


    public bpmn2_Message(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_CorrelationPropertyRetrievalExpression getBpmn2_correlationpropertyretrievalexpression() {
        return bpmn2_correlationpropertyretrievalexpression;
    }

    public void setBpmn2_correlationpropertyretrievalexpression(bpmn2_CorrelationPropertyRetrievalExpression bpmn2_correlationpropertyretrievalexpression) {
        this.bpmn2_correlationpropertyretrievalexpression = bpmn2_correlationpropertyretrievalexpression;
    }
    public bpmn2_MessageFlow getBpmn2_messageflow() {
        return bpmn2_messageflow;
    }

    public void setBpmn2_messageflow(bpmn2_MessageFlow bpmn2_messageflow) {
        this.bpmn2_messageflow = bpmn2_messageflow;
    }
    public bpmn2_Operation getBpmn2_operation() {
        return bpmn2_operation;
    }

    public void setBpmn2_operation(bpmn2_Operation bpmn2_operation) {
        this.bpmn2_operation = bpmn2_operation;
    }
    public bpmn2_Operation getBpmn2_operation() {
        return bpmn2_operation;
    }

    public void setBpmn2_operation(bpmn2_Operation bpmn2_operation) {
        this.bpmn2_operation = bpmn2_operation;
    }

}
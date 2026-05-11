





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CorrelationPropertyRetrievalExpression extends BaseElement {






    private bpmn2_CorrelationProperty bpmn2_correlationproperty;




    private bpmn2_Message bpmn2_message;


    public bpmn2_CorrelationPropertyRetrievalExpression(
    ) {
        super(
        );
    }



    public bpmn2_CorrelationProperty getBpmn2_correlationproperty() {
        return bpmn2_correlationproperty;
    }

    public void setBpmn2_correlationproperty(bpmn2_CorrelationProperty bpmn2_correlationproperty) {
        this.bpmn2_correlationproperty = bpmn2_correlationproperty;
    }
    public bpmn2_Message getBpmn2_message() {
        return bpmn2_message;
    }

    public void setBpmn2_message(bpmn2_Message bpmn2_message) {
        this.bpmn2_message = bpmn2_message;
    }

}
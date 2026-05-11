





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ItemDefinition extends RootElement {

    private String itemKind;
    private boolean isCollection;





    private bpmn2_Message bpmn2_message;




    private bpmn2_Signal bpmn2_signal;




    private bpmn2_Escalation bpmn2_escalation;




    private bpmn2_CorrelationProperty bpmn2_correlationproperty;




    private bpmn2_Error bpmn2_error;


    public bpmn2_ItemDefinition(
        String itemKind,        boolean isCollection    ) {
        super(
        );
        this.itemKind = itemKind;
        this.isCollection = isCollection;
    }


    public String getItemkind() {
        return itemKind;
    }

    public void setItemkind(String itemKind) {
        this.itemKind = itemKind;
    }
    public boolean getIscollection() {
        return isCollection;
    }

    public void setIscollection(boolean isCollection) {
        this.isCollection = isCollection;
    }

    public bpmn2_Message getBpmn2_message() {
        return bpmn2_message;
    }

    public void setBpmn2_message(bpmn2_Message bpmn2_message) {
        this.bpmn2_message = bpmn2_message;
    }
    public bpmn2_Signal getBpmn2_signal() {
        return bpmn2_signal;
    }

    public void setBpmn2_signal(bpmn2_Signal bpmn2_signal) {
        this.bpmn2_signal = bpmn2_signal;
    }
    public bpmn2_Escalation getBpmn2_escalation() {
        return bpmn2_escalation;
    }

    public void setBpmn2_escalation(bpmn2_Escalation bpmn2_escalation) {
        this.bpmn2_escalation = bpmn2_escalation;
    }
    public bpmn2_CorrelationProperty getBpmn2_correlationproperty() {
        return bpmn2_correlationproperty;
    }

    public void setBpmn2_correlationproperty(bpmn2_CorrelationProperty bpmn2_correlationproperty) {
        this.bpmn2_correlationproperty = bpmn2_correlationproperty;
    }
    public bpmn2_Error getBpmn2_error() {
        return bpmn2_error;
    }

    public void setBpmn2_error(bpmn2_Error bpmn2_error) {
        this.bpmn2_error = bpmn2_error;
    }

}
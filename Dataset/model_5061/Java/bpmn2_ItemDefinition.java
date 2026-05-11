





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ItemDefinition extends RootElement {

    private boolean isCollection;
    private String itemKind;





    private bpmn2_Message bpmn2_message;




    private bpmn2_ResourceParameter bpmn2_resourceparameter;




    private bpmn2_EObject bpmn2_eobject;




    private bpmn2_Signal bpmn2_signal;




    private bpmn2_ItemAwareElement bpmn2_itemawareelement;


    public bpmn2_ItemDefinition(
        boolean isCollection,        String itemKind    ) {
        super(
        );
        this.isCollection = isCollection;
        this.itemKind = itemKind;
    }


    public boolean getIscollection() {
        return isCollection;
    }

    public void setIscollection(boolean isCollection) {
        this.isCollection = isCollection;
    }
    public String getItemkind() {
        return itemKind;
    }

    public void setItemkind(String itemKind) {
        this.itemKind = itemKind;
    }

    public bpmn2_Message getBpmn2_message() {
        return bpmn2_message;
    }

    public void setBpmn2_message(bpmn2_Message bpmn2_message) {
        this.bpmn2_message = bpmn2_message;
    }
    public bpmn2_ResourceParameter getBpmn2_resourceparameter() {
        return bpmn2_resourceparameter;
    }

    public void setBpmn2_resourceparameter(bpmn2_ResourceParameter bpmn2_resourceparameter) {
        this.bpmn2_resourceparameter = bpmn2_resourceparameter;
    }
    public bpmn2_EObject getBpmn2_eobject() {
        return bpmn2_eobject;
    }

    public void setBpmn2_eobject(bpmn2_EObject bpmn2_eobject) {
        this.bpmn2_eobject = bpmn2_eobject;
    }
    public bpmn2_Signal getBpmn2_signal() {
        return bpmn2_signal;
    }

    public void setBpmn2_signal(bpmn2_Signal bpmn2_signal) {
        this.bpmn2_signal = bpmn2_signal;
    }
    public bpmn2_ItemAwareElement getBpmn2_itemawareelement() {
        return bpmn2_itemawareelement;
    }

    public void setBpmn2_itemawareelement(bpmn2_ItemAwareElement bpmn2_itemawareelement) {
        this.bpmn2_itemawareelement = bpmn2_itemawareelement;
    }

}






import java.util.List;
import java.util.ArrayList;

public class bpmn2_ItemDefinition extends RootElement {

    private boolean isCollection;
    private String itemKind;





    private bpmn2_Message bpmn2_message;


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

}






import java.util.List;
import java.util.ArrayList;

public class bpmn2_Collaboration extends RootElement {

    private boolean isClosed;
    private String name;





    private bpmn2_CallConversation bpmn2_callconversation;


    public bpmn2_Collaboration(
        boolean isClosed,        String name    ) {
        super(
        );
        this.isClosed = isClosed;
        this.name = name;
    }


    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_CallConversation getBpmn2_callconversation() {
        return bpmn2_callconversation;
    }

    public void setBpmn2_callconversation(bpmn2_CallConversation bpmn2_callconversation) {
        this.bpmn2_callconversation = bpmn2_callconversation;
    }

}
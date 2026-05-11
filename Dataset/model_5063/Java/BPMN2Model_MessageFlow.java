





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_MessageFlow extends BaseElement {

    private String name;





    private BPMN2Model_Message bpmn2model_message;


    public BPMN2Model_MessageFlow(
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

    public BPMN2Model_Message getBpmn2model_message() {
        return bpmn2model_message;
    }

    public void setBpmn2model_message(BPMN2Model_Message bpmn2model_message) {
        this.bpmn2model_message = bpmn2model_message;
    }

}
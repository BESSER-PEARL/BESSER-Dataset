





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_FlowElement extends BaseElement {

    private String name;





    private BPMN2Model_Monitoring bpmn2model_monitoring;


    public BPMN2Model_FlowElement(
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

    public BPMN2Model_Monitoring getBpmn2model_monitoring() {
        return bpmn2model_monitoring;
    }

    public void setBpmn2model_monitoring(BPMN2Model_Monitoring bpmn2model_monitoring) {
        this.bpmn2model_monitoring = bpmn2model_monitoring;
    }

}
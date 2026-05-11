





import java.util.List;
import java.util.ArrayList;

public class bpmn2_FlowElement extends BaseElement {

    private String name;





    private bpmn2_Auditing bpmn2_auditing;




    private bpmn2_Monitoring bpmn2_monitoring;


    public bpmn2_FlowElement(
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

    public bpmn2_Auditing getBpmn2_auditing() {
        return bpmn2_auditing;
    }

    public void setBpmn2_auditing(bpmn2_Auditing bpmn2_auditing) {
        this.bpmn2_auditing = bpmn2_auditing;
    }
    public bpmn2_Monitoring getBpmn2_monitoring() {
        return bpmn2_monitoring;
    }

    public void setBpmn2_monitoring(bpmn2_Monitoring bpmn2_monitoring) {
        this.bpmn2_monitoring = bpmn2_monitoring;
    }

}
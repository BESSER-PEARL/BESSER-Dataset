





import java.util.List;
import java.util.ArrayList;

public class bpmn2_FlowElement extends BaseElement {

    private String name;





    private bpmn2_CategoryValue bpmn2_categoryvalue;




    private List<bpmn2_CategoryValue> bpmn2_categoryvalues;




    private bpmn2_Monitoring bpmn2_monitoring;




    private bpmn2_FlowElementsContainer bpmn2_flowelementscontainer;




    private bpmn2_Auditing bpmn2_auditing;


    public bpmn2_FlowElement(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_categoryvalues = new ArrayList<>();
    }

    public bpmn2_FlowElement(
        String name        ArrayList<bpmn2_CategoryValue> bpmn2_categoryvalues    ) {
        this.name = name;
        this.bpmn2_categoryvalues = bpmn2_categoryvalues;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_CategoryValue getBpmn2_categoryvalue() {
        return bpmn2_categoryvalue;
    }

    public void setBpmn2_categoryvalue(bpmn2_CategoryValue bpmn2_categoryvalue) {
        this.bpmn2_categoryvalue = bpmn2_categoryvalue;
    }
    public List<bpmn2_CategoryValue> getBpmn2_categoryvalues() {
        return bpmn2_categoryvalues;
    }

    public void addBpmn2_categoryvalue(Bpmn2_categoryvalue bpmn2_categoryvalue) {
        this.bpmn2_categoryvalues.add(bpmn2_categoryvalue);
    }
    public bpmn2_Monitoring getBpmn2_monitoring() {
        return bpmn2_monitoring;
    }

    public void setBpmn2_monitoring(bpmn2_Monitoring bpmn2_monitoring) {
        this.bpmn2_monitoring = bpmn2_monitoring;
    }
    public bpmn2_FlowElementsContainer getBpmn2_flowelementscontainer() {
        return bpmn2_flowelementscontainer;
    }

    public void setBpmn2_flowelementscontainer(bpmn2_FlowElementsContainer bpmn2_flowelementscontainer) {
        this.bpmn2_flowelementscontainer = bpmn2_flowelementscontainer;
    }
    public bpmn2_Auditing getBpmn2_auditing() {
        return bpmn2_auditing;
    }

    public void setBpmn2_auditing(bpmn2_Auditing bpmn2_auditing) {
        this.bpmn2_auditing = bpmn2_auditing;
    }

}
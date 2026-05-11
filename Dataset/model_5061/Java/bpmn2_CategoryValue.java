





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CategoryValue extends BaseElement {

    private String value;





    private bpmn2_FlowElement bpmn2_flowelement;




    private List<bpmn2_FlowElement> bpmn2_flowelements;


    public bpmn2_CategoryValue(
        String value    ) {
        super(
        );
        this.value = value;
        this.bpmn2_flowelements = new ArrayList<>();
    }

    public bpmn2_CategoryValue(
        String value        ArrayList<bpmn2_FlowElement> bpmn2_flowelements    ) {
        this.value = value;
        this.bpmn2_flowelements = bpmn2_flowelements;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public bpmn2_FlowElement getBpmn2_flowelement() {
        return bpmn2_flowelement;
    }

    public void setBpmn2_flowelement(bpmn2_FlowElement bpmn2_flowelement) {
        this.bpmn2_flowelement = bpmn2_flowelement;
    }
    public List<bpmn2_FlowElement> getBpmn2_flowelements() {
        return bpmn2_flowelements;
    }

    public void addBpmn2_flowelement(Bpmn2_flowelement bpmn2_flowelement) {
        this.bpmn2_flowelements.add(bpmn2_flowelement);
    }

}
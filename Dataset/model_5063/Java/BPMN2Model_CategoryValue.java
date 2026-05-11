





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_CategoryValue extends BaseElement {

    private String value;





    private BPMN2Model_FlowElement bpmn2model_flowelement;




    private List<BPMN2Model_FlowElement> bpmn2model_flowelements;


    public BPMN2Model_CategoryValue(
        String value    ) {
        super(
        );
        this.value = value;
        this.bpmn2model_flowelements = new ArrayList<>();
    }

    public BPMN2Model_CategoryValue(
        String value        ArrayList<BPMN2Model_FlowElement> bpmn2model_flowelements    ) {
        this.value = value;
        this.bpmn2model_flowelements = bpmn2model_flowelements;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public BPMN2Model_FlowElement getBpmn2model_flowelement() {
        return bpmn2model_flowelement;
    }

    public void setBpmn2model_flowelement(BPMN2Model_FlowElement bpmn2model_flowelement) {
        this.bpmn2model_flowelement = bpmn2model_flowelement;
    }
    public List<BPMN2Model_FlowElement> getBpmn2model_flowelements() {
        return bpmn2model_flowelements;
    }

    public void addBpmn2model_flowelement(Bpmn2model_flowelement bpmn2model_flowelement) {
        this.bpmn2model_flowelements.add(bpmn2model_flowelement);
    }

}
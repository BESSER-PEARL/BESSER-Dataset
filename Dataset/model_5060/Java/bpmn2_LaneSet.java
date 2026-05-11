





import java.util.List;
import java.util.ArrayList;

public class bpmn2_LaneSet extends BaseElement {

    private String name;





    private bpmn2_FlowElementsContainer bpmn2_flowelementscontainer;


    public bpmn2_LaneSet(
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

    public bpmn2_FlowElementsContainer getBpmn2_flowelementscontainer() {
        return bpmn2_flowelementscontainer;
    }

    public void setBpmn2_flowelementscontainer(bpmn2_FlowElementsContainer bpmn2_flowelementscontainer) {
        this.bpmn2_flowelementscontainer = bpmn2_flowelementscontainer;
    }

}
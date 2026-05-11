





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Event extends FlowNode, InteractionNode {






    private List<bpmn2_Property> bpmn2_propertys;


    public bpmn2_Event(
    ) {
        super(
        );
        this.bpmn2_propertys = new ArrayList<>();
    }

    public bpmn2_Event(
        ArrayList<bpmn2_Property> bpmn2_propertys    ) {
        this.bpmn2_propertys = bpmn2_propertys;
    }


    public List<bpmn2_Property> getBpmn2_propertys() {
        return bpmn2_propertys;
    }

    public void addBpmn2_property(Bpmn2_property bpmn2_property) {
        this.bpmn2_propertys.add(bpmn2_property);
    }

}
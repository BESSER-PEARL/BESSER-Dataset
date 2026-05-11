





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Event extends FlowNode, InteractionNode {






    private List<BPMN2Model_Property> bpmn2model_propertys;


    public BPMN2Model_Event(
    ) {
        super(
        );
        this.bpmn2model_propertys = new ArrayList<>();
    }

    public BPMN2Model_Event(
        ArrayList<BPMN2Model_Property> bpmn2model_propertys    ) {
        this.bpmn2model_propertys = bpmn2model_propertys;
    }


    public List<BPMN2Model_Property> getBpmn2model_propertys() {
        return bpmn2model_propertys;
    }

    public void addBpmn2model_property(Bpmn2model_property bpmn2model_property) {
        this.bpmn2model_propertys.add(bpmn2model_property);
    }

}
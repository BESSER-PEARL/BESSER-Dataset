





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Signal extends RootElement {

    private String name;





    private BPMN2Model_ItemDefinition bpmn2model_itemdefinition;


    public BPMN2Model_Signal(
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

    public BPMN2Model_ItemDefinition getBpmn2model_itemdefinition() {
        return bpmn2model_itemdefinition;
    }

    public void setBpmn2model_itemdefinition(BPMN2Model_ItemDefinition bpmn2model_itemdefinition) {
        this.bpmn2model_itemdefinition = bpmn2model_itemdefinition;
    }

}
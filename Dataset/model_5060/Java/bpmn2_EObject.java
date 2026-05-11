





import java.util.List;
import java.util.ArrayList;

public class bpmn2_EObject  {






    private bpmn2_Interface bpmn2_interface;




    private bpmn2_ItemDefinition bpmn2_itemdefinition;




    private bpmn2_Operation bpmn2_operation;


    public bpmn2_EObject(
    ) {
    }



    public bpmn2_Interface getBpmn2_interface() {
        return bpmn2_interface;
    }

    public void setBpmn2_interface(bpmn2_Interface bpmn2_interface) {
        this.bpmn2_interface = bpmn2_interface;
    }
    public bpmn2_ItemDefinition getBpmn2_itemdefinition() {
        return bpmn2_itemdefinition;
    }

    public void setBpmn2_itemdefinition(bpmn2_ItemDefinition bpmn2_itemdefinition) {
        this.bpmn2_itemdefinition = bpmn2_itemdefinition;
    }
    public bpmn2_Operation getBpmn2_operation() {
        return bpmn2_operation;
    }

    public void setBpmn2_operation(bpmn2_Operation bpmn2_operation) {
        this.bpmn2_operation = bpmn2_operation;
    }

}
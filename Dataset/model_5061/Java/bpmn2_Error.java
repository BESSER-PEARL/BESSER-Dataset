





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Error extends RootElement {

    private String name;
    private String errorCode;





    private bpmn2_Operation bpmn2_operation;




    private bpmn2_ItemDefinition bpmn2_itemdefinition;


    public bpmn2_Error(
        String name,        String errorCode    ) {
        super(
        );
        this.name = name;
        this.errorCode = errorCode;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getErrorcode() {
        return errorCode;
    }

    public void setErrorcode(String errorCode) {
        this.errorCode = errorCode;
    }

    public bpmn2_Operation getBpmn2_operation() {
        return bpmn2_operation;
    }

    public void setBpmn2_operation(bpmn2_Operation bpmn2_operation) {
        this.bpmn2_operation = bpmn2_operation;
    }
    public bpmn2_ItemDefinition getBpmn2_itemdefinition() {
        return bpmn2_itemdefinition;
    }

    public void setBpmn2_itemdefinition(bpmn2_ItemDefinition bpmn2_itemdefinition) {
        this.bpmn2_itemdefinition = bpmn2_itemdefinition;
    }

}
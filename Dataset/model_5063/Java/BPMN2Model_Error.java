





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Error extends RootElement {

    private String errorCode;
    private String name;





    private BPMN2Model_ItemDefinition bpmn2model_itemdefinition;




    private BPMN2Model_Operation bpmn2model_operation;


    public BPMN2Model_Error(
        String errorCode,        String name    ) {
        super(
        );
        this.errorCode = errorCode;
        this.name = name;
    }


    public String getErrorcode() {
        return errorCode;
    }

    public void setErrorcode(String errorCode) {
        this.errorCode = errorCode;
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
    public BPMN2Model_Operation getBpmn2model_operation() {
        return bpmn2model_operation;
    }

    public void setBpmn2model_operation(BPMN2Model_Operation bpmn2model_operation) {
        this.bpmn2model_operation = bpmn2model_operation;
    }

}
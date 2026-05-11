





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Error extends RootElement {

    private String errorCode;
    private String name;





    private bpmn2_ItemDefinition bpmn2_itemdefinition;


    public bpmn2_Error(
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

    public bpmn2_ItemDefinition getBpmn2_itemdefinition() {
        return bpmn2_itemdefinition;
    }

    public void setBpmn2_itemdefinition(bpmn2_ItemDefinition bpmn2_itemdefinition) {
        this.bpmn2_itemdefinition = bpmn2_itemdefinition;
    }

}
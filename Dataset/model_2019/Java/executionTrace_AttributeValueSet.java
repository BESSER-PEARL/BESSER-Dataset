





import java.util.List;
import java.util.ArrayList;

public class executionTrace_AttributeValueSet extends Execution {

    private String instanceObject;
    private String newValue;



    public executionTrace_AttributeValueSet(
        String instanceObject,        String newValue    ) {
        super(
        );
        this.instanceObject = instanceObject;
        this.newValue = newValue;
    }


    public String getInstanceobject() {
        return instanceObject;
    }

    public void setInstanceobject(String instanceObject) {
        this.instanceObject = instanceObject;
    }
    public String getNewvalue() {
        return newValue;
    }

    public void setNewvalue(String newValue) {
        this.newValue = newValue;
    }


}
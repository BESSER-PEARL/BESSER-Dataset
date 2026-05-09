





import java.util.List;
import java.util.ArrayList;

public class statemachines_BooleanAttributeValue extends AttributeValue {

    private String value;





    private statemachines_BooleanAttribute statemachines_booleanattribute;


    public statemachines_BooleanAttributeValue(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public statemachines_BooleanAttribute getStatemachines_booleanattribute() {
        return statemachines_booleanattribute;
    }

    public void setStatemachines_booleanattribute(statemachines_BooleanAttribute statemachines_booleanattribute) {
        this.statemachines_booleanattribute = statemachines_booleanattribute;
    }

}
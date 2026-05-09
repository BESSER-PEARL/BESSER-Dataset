





import java.util.List;
import java.util.ArrayList;

public class statemachines_StringAttributeValue extends AttributeValue {

    private String value;





    private statemachines_StringAttribute statemachines_stringattribute;


    public statemachines_StringAttributeValue(
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

    public statemachines_StringAttribute getStatemachines_stringattribute() {
        return statemachines_stringattribute;
    }

    public void setStatemachines_stringattribute(statemachines_StringAttribute statemachines_stringattribute) {
        this.statemachines_stringattribute = statemachines_stringattribute;
    }

}
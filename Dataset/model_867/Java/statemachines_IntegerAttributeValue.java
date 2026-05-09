





import java.util.List;
import java.util.ArrayList;

public class statemachines_IntegerAttributeValue extends AttributeValue {

    private String value;





    private statemachines_IntegerAttribute statemachines_integerattribute;


    public statemachines_IntegerAttributeValue(
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

    public statemachines_IntegerAttribute getStatemachines_integerattribute() {
        return statemachines_integerattribute;
    }

    public void setStatemachines_integerattribute(statemachines_IntegerAttribute statemachines_integerattribute) {
        this.statemachines_integerattribute = statemachines_integerattribute;
    }

}






import java.util.List;
import java.util.ArrayList;

public class simplestatechart101_Variable extends Thing {

    private String type;
    private String value;





    private simplestatechart101_State simplestatechart101_state;


    public simplestatechart101_Variable(
        String type,        String value    ) {
        super(
        );
        this.type = type;
        this.value = value;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public simplestatechart101_State getSimplestatechart101_state() {
        return simplestatechart101_state;
    }

    public void setSimplestatechart101_state(simplestatechart101_State simplestatechart101_state) {
        this.simplestatechart101_state = simplestatechart101_state;
    }

}
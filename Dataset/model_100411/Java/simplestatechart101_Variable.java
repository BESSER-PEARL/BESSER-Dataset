





import java.util.List;
import java.util.ArrayList;

public class simplestatechart101_Variable extends Thing {

    private String value;
    private String type;





    private simplestatechart101_State simplestatechart101_state;


    public simplestatechart101_Variable(
        String value,        String type    ) {
        super(
        );
        this.value = value;
        this.type = type;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public simplestatechart101_State getSimplestatechart101_state() {
        return simplestatechart101_state;
    }

    public void setSimplestatechart101_state(simplestatechart101_State simplestatechart101_state) {
        this.simplestatechart101_state = simplestatechart101_state;
    }

}
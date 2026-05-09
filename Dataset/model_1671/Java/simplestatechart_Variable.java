





import java.util.List;
import java.util.ArrayList;

public class simplestatechart_Variable extends Thing {

    private String type;
    private String value;





    private simplestatechart_State simplestatechart_state;


    public simplestatechart_Variable(
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

    public simplestatechart_State getSimplestatechart_state() {
        return simplestatechart_state;
    }

    public void setSimplestatechart_state(simplestatechart_State simplestatechart_state) {
        this.simplestatechart_state = simplestatechart_state;
    }

}
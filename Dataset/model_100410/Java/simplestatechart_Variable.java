





import java.util.List;
import java.util.ArrayList;

public class simplestatechart_Variable extends Thing {

    private String value;
    private String type;





    private simplestatechart_State simplestatechart_state;


    public simplestatechart_Variable(
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

    public simplestatechart_State getSimplestatechart_state() {
        return simplestatechart_state;
    }

    public void setSimplestatechart_state(simplestatechart_State simplestatechart_state) {
        this.simplestatechart_state = simplestatechart_state;
    }

}
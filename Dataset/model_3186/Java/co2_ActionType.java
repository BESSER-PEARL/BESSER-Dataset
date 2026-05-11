





import java.util.List;
import java.util.ArrayList;

public class co2_ActionType  {

    private String value;





    private co2_Action co2_action;


    public co2_ActionType(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public co2_Action getCo2_action() {
        return co2_action;
    }

    public void setCo2_action(co2_Action co2_action) {
        this.co2_action = co2_action;
    }

}
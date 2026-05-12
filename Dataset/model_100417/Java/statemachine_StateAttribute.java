





import java.util.List;
import java.util.ArrayList;

public class statemachine_StateAttribute  {

    private String type;
    private String value;





    private statemachine_StateChange statemachine_statechange;




    private statemachine_StateAttribute statemachine_stateattribute;


    public statemachine_StateAttribute(
        String type,        String value    ) {
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

    public statemachine_StateChange getStatemachine_statechange() {
        return statemachine_statechange;
    }

    public void setStatemachine_statechange(statemachine_StateChange statemachine_statechange) {
        this.statemachine_statechange = statemachine_statechange;
    }
    public statemachine_StateAttribute getStatemachine_stateattribute() {
        return statemachine_stateattribute;
    }

    public void setStatemachine_stateattribute(statemachine_StateAttribute statemachine_stateattribute) {
        this.statemachine_stateattribute = statemachine_stateattribute;
    }

}
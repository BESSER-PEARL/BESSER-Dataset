





import java.util.List;
import java.util.ArrayList;

public class behaviour_Condition  {

    private String value;
    private String operation;
    private String key;





    private behaviour_Choice behaviour_choice;


    public behaviour_Condition(
        String value,        String operation,        String key    ) {
        this.value = value;
        this.operation = operation;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getOperation() {
        return operation;
    }

    public void setOperation(String operation) {
        this.operation = operation;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public behaviour_Choice getBehaviour_choice() {
        return behaviour_choice;
    }

    public void setBehaviour_choice(behaviour_Choice behaviour_choice) {
        this.behaviour_choice = behaviour_choice;
    }

}
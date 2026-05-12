





import java.util.List;
import java.util.ArrayList;

public class statechart101_Variable extends NamedElement, Thing {

    private String type;
    private String value;





    private statechart101_State statechart101_state;


    public statechart101_Variable(
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

    public statechart101_State getStatechart101_state() {
        return statechart101_state;
    }

    public void setStatechart101_state(statechart101_State statechart101_state) {
        this.statechart101_state = statechart101_state;
    }

}
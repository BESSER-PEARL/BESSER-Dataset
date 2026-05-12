





import java.util.List;
import java.util.ArrayList;

public class statechart101_Variable extends NamedElement, Thing {

    private String value;
    private String type;





    private statechart101_State statechart101_state;


    public statechart101_Variable(
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

    public statechart101_State getStatechart101_state() {
        return statechart101_state;
    }

    public void setStatechart101_state(statechart101_State statechart101_state) {
        this.statechart101_state = statechart101_state;
    }

}
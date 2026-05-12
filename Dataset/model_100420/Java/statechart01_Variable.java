





import java.util.List;
import java.util.ArrayList;

public class statechart01_Variable  {

    private String name;
    private String value;
    private String type;





    private statechart01_State statechart01_state;


    public statechart01_Variable(
        String name,        String value,        String type    ) {
        this.name = name;
        this.value = value;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public statechart01_State getStatechart01_state() {
        return statechart01_state;
    }

    public void setStatechart01_state(statechart01_State statechart01_state) {
        this.statechart01_state = statechart01_state;
    }

}
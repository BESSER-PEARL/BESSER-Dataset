





import java.util.List;
import java.util.ArrayList;

public class statechart00_Variable  {

    private String type;
    private String name;
    private String value;





    private statechart00_State statechart00_state;


    public statechart00_Variable(
        String type,        String name,        String value    ) {
        this.type = type;
        this.name = name;
        this.value = value;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
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

    public statechart00_State getStatechart00_state() {
        return statechart00_state;
    }

    public void setStatechart00_state(statechart00_State statechart00_state) {
        this.statechart00_state = statechart00_state;
    }

}
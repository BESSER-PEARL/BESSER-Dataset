





import java.util.List;
import java.util.ArrayList;

public class fsm_Variable  {

    private String name;
    private boolean value;



    public fsm_Variable(
        String name,        boolean value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}
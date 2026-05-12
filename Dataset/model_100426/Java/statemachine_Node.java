





import java.util.List;
import java.util.ArrayList;

public class statemachine_Node  {

    private String name;
    private int id;





    private statemachine_Region statemachine_region;


    public statemachine_Node(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public statemachine_Region getStatemachine_region() {
        return statemachine_region;
    }

    public void setStatemachine_region(statemachine_Region statemachine_region) {
        this.statemachine_region = statemachine_region;
    }

}
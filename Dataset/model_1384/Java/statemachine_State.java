





import java.util.List;
import java.util.ArrayList;

public class statemachine_State extends Vertex {

    private String name;





    private statemachine_Region statemachine_region;




    private statemachine_ComplexState statemachine_complexstate;


    public statemachine_State(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_Region getStatemachine_region() {
        return statemachine_region;
    }

    public void setStatemachine_region(statemachine_Region statemachine_region) {
        this.statemachine_region = statemachine_region;
    }
    public statemachine_ComplexState getStatemachine_complexstate() {
        return statemachine_complexstate;
    }

    public void setStatemachine_complexstate(statemachine_ComplexState statemachine_complexstate) {
        this.statemachine_complexstate = statemachine_complexstate;
    }

}
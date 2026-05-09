





import java.util.List;
import java.util.ArrayList;

public class statesml_Node  {

    private String name;





    private statesml_StateSystem statesml_statesystem;


    public statesml_Node(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statesml_StateSystem getStatesml_statesystem() {
        return statesml_statesystem;
    }

    public void setStatesml_statesystem(statesml_StateSystem statesml_statesystem) {
        this.statesml_statesystem = statesml_statesystem;
    }

}
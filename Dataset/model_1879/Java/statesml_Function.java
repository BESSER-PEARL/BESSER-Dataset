





import java.util.List;
import java.util.ArrayList;

public class statesml_Function  {

    private String name;





    private statesml_SystemUnits statesml_systemunits;




    private statesml_Node statesml_node;


    public statesml_Function(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statesml_SystemUnits getStatesml_systemunits() {
        return statesml_systemunits;
    }

    public void setStatesml_systemunits(statesml_SystemUnits statesml_systemunits) {
        this.statesml_systemunits = statesml_systemunits;
    }
    public statesml_Node getStatesml_node() {
        return statesml_node;
    }

    public void setStatesml_node(statesml_Node statesml_node) {
        this.statesml_node = statesml_node;
    }

}
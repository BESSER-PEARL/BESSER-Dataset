





import java.util.List;
import java.util.ArrayList;

public class statesml_Attribute  {

    private String name;





    private statesml_DataType statesml_datatype;




    private statesml_SystemUnits statesml_systemunits;


    public statesml_Attribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statesml_DataType getStatesml_datatype() {
        return statesml_datatype;
    }

    public void setStatesml_datatype(statesml_DataType statesml_datatype) {
        this.statesml_datatype = statesml_datatype;
    }
    public statesml_SystemUnits getStatesml_systemunits() {
        return statesml_systemunits;
    }

    public void setStatesml_systemunits(statesml_SystemUnits statesml_systemunits) {
        this.statesml_systemunits = statesml_systemunits;
    }

}
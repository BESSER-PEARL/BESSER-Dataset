





import java.util.List;
import java.util.ArrayList;

public class statesml_DataType  {

    private String name;





    private statesml_Attribute statesml_attribute;


    public statesml_DataType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statesml_Attribute getStatesml_attribute() {
        return statesml_attribute;
    }

    public void setStatesml_attribute(statesml_Attribute statesml_attribute) {
        this.statesml_attribute = statesml_attribute;
    }

}
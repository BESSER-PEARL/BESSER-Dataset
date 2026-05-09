





import java.util.List;
import java.util.ArrayList;

public class statesml_KeyValuePair  {

    private String name;





    private statesml_DataType statesml_datatype;


    public statesml_KeyValuePair(
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

}
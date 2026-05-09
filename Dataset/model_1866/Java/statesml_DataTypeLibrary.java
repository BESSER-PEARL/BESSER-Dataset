





import java.util.List;
import java.util.ArrayList;

public class statesml_DataTypeLibrary  {

    private String name;





    private List<statesml_DataType> statesml_datatypes;


    public statesml_DataTypeLibrary(
        String name    ) {
        this.name = name;
        this.statesml_datatypes = new ArrayList<>();
    }

    public statesml_DataTypeLibrary(
        String name        ArrayList<statesml_DataType> statesml_datatypes    ) {
        this.name = name;
        this.statesml_datatypes = statesml_datatypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statesml_DataType> getStatesml_datatypes() {
        return statesml_datatypes;
    }

    public void addStatesml_datatype(Statesml_datatype statesml_datatype) {
        this.statesml_datatypes.add(statesml_datatype);
    }

}
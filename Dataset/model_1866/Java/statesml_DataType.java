





import java.util.List;
import java.util.ArrayList;

public class statesml_DataType  {

    private String name;





    private List<statesml_Function> statesml_functions;


    public statesml_DataType(
        String name    ) {
        this.name = name;
        this.statesml_functions = new ArrayList<>();
    }

    public statesml_DataType(
        String name        ArrayList<statesml_Function> statesml_functions    ) {
        this.name = name;
        this.statesml_functions = statesml_functions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statesml_Function> getStatesml_functions() {
        return statesml_functions;
    }

    public void addStatesml_function(Statesml_function statesml_function) {
        this.statesml_functions.add(statesml_function);
    }

}
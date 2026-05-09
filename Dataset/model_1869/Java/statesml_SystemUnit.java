





import java.util.List;
import java.util.ArrayList;

public class statesml_SystemUnit  {

    private String name;





    private List<statesml_Attribute> statesml_attributes;




    private statesml_SystemUnitLibrary statesml_systemunitlibrary;




    private List<statesml_Function> statesml_functions;


    public statesml_SystemUnit(
        String name    ) {
        this.name = name;
        this.statesml_attributes = new ArrayList<>();
        this.statesml_functions = new ArrayList<>();
    }

    public statesml_SystemUnit(
        String name        ArrayList<statesml_Attribute> statesml_attributes,        ArrayList<statesml_Function> statesml_functions    ) {
        this.name = name;
        this.statesml_attributes = statesml_attributes;
        this.statesml_functions = statesml_functions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<statesml_Attribute> getStatesml_attributes() {
        return statesml_attributes;
    }

    public void addStatesml_attribute(Statesml_attribute statesml_attribute) {
        this.statesml_attributes.add(statesml_attribute);
    }
    public statesml_SystemUnitLibrary getStatesml_systemunitlibrary() {
        return statesml_systemunitlibrary;
    }

    public void setStatesml_systemunitlibrary(statesml_SystemUnitLibrary statesml_systemunitlibrary) {
        this.statesml_systemunitlibrary = statesml_systemunitlibrary;
    }
    public List<statesml_Function> getStatesml_functions() {
        return statesml_functions;
    }

    public void addStatesml_function(Statesml_function statesml_function) {
        this.statesml_functions.add(statesml_function);
    }

}
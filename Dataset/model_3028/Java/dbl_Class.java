





import java.util.List;
import java.util.ArrayList;

public class dbl_Class extends Concept, Type, AnnotateableElement, ConstructiveExtensionAtContentExtensionPoint, Construct, NamedElement {

    private boolean active;





    private dbl_Module dbl_module;




    private List<dbl_Variable> dbl_variables;




    private List<dbl_Function> dbl_functions;


    public dbl_Class(
        boolean active    ) {
        super(
        );
        this.active = active;
        this.dbl_variables = new ArrayList<>();
        this.dbl_functions = new ArrayList<>();
    }

    public dbl_Class(
        boolean active        ArrayList<dbl_Variable> dbl_variables,        ArrayList<dbl_Function> dbl_functions    ) {
        this.active = active;
        this.dbl_variables = dbl_variables;
        this.dbl_functions = dbl_functions;
    }

    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }
    public List<dbl_Variable> getDbl_variables() {
        return dbl_variables;
    }

    public void addDbl_variable(Dbl_variable dbl_variable) {
        this.dbl_variables.add(dbl_variable);
    }
    public List<dbl_Function> getDbl_functions() {
        return dbl_functions;
    }

    public void addDbl_function(Dbl_function dbl_function) {
        this.dbl_functions.add(dbl_function);
    }

}
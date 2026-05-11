





import java.util.List;
import java.util.ArrayList;

public class dbl_Class extends LanguageConceptClassifier, Construct, Type, NamedElement, ConstructiveExtensionAtContentExtensionPoint {

    private boolean active;





    private List<dbl_Function> dbl_functions;




    private dbl_Module dbl_module;


    public dbl_Class(
        boolean active    ) {
        super(
        );
        this.active = active;
        this.dbl_functions = new ArrayList<>();
    }

    public dbl_Class(
        boolean active        ArrayList<dbl_Function> dbl_functions    ) {
        this.active = active;
        this.dbl_functions = dbl_functions;
    }

    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public List<dbl_Function> getDbl_functions() {
        return dbl_functions;
    }

    public void addDbl_function(Dbl_function dbl_function) {
        this.dbl_functions.add(dbl_function);
    }
    public dbl_Module getDbl_module() {
        return dbl_module;
    }

    public void setDbl_module(dbl_Module dbl_module) {
        this.dbl_module = dbl_module;
    }

}






import java.util.List;
import java.util.ArrayList;

public class dbl_Module extends ConstructiveExtensionAtContentExtensionPoint, Construct, NamedElement {






    private List<dbl_Function> dbl_functions;




    private List<dbl_ExtensionSemantics> dbl_extensionsemanticss;




    private List<dbl_Variable> dbl_variables;




    private List<dbl_Extension> dbl_extensions;


    public dbl_Module(
    ) {
        super(
        );
        this.dbl_functions = new ArrayList<>();
        this.dbl_extensionsemanticss = new ArrayList<>();
        this.dbl_variables = new ArrayList<>();
        this.dbl_extensions = new ArrayList<>();
    }

    public dbl_Module(
        ArrayList<dbl_Function> dbl_functions,        ArrayList<dbl_ExtensionSemantics> dbl_extensionsemanticss,        ArrayList<dbl_Variable> dbl_variables,        ArrayList<dbl_Extension> dbl_extensions    ) {
        this.dbl_functions = dbl_functions;
        this.dbl_extensionsemanticss = dbl_extensionsemanticss;
        this.dbl_variables = dbl_variables;
        this.dbl_extensions = dbl_extensions;
    }


    public List<dbl_Function> getDbl_functions() {
        return dbl_functions;
    }

    public void addDbl_function(Dbl_function dbl_function) {
        this.dbl_functions.add(dbl_function);
    }
    public List<dbl_ExtensionSemantics> getDbl_extensionsemanticss() {
        return dbl_extensionsemanticss;
    }

    public void addDbl_extensionsemantics(Dbl_extensionsemantics dbl_extensionsemantics) {
        this.dbl_extensionsemanticss.add(dbl_extensionsemantics);
    }
    public List<dbl_Variable> getDbl_variables() {
        return dbl_variables;
    }

    public void addDbl_variable(Dbl_variable dbl_variable) {
        this.dbl_variables.add(dbl_variable);
    }
    public List<dbl_Extension> getDbl_extensions() {
        return dbl_extensions;
    }

    public void addDbl_extension(Dbl_extension dbl_extension) {
        this.dbl_extensions.add(dbl_extension);
    }

}
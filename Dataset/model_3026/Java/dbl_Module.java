





import java.util.List;
import java.util.ArrayList;

public class dbl_Module extends NamedElement, Construct, ConstructiveExtensionAtContentExtensionPoint {






    private List<dbl_Function> dbl_functions;


    public dbl_Module(
    ) {
        super(
        );
        this.dbl_functions = new ArrayList<>();
    }

    public dbl_Module(
        ArrayList<dbl_Function> dbl_functions    ) {
        this.dbl_functions = dbl_functions;
    }


    public List<dbl_Function> getDbl_functions() {
        return dbl_functions;
    }

    public void addDbl_function(Dbl_function dbl_function) {
        this.dbl_functions.add(dbl_function);
    }

}
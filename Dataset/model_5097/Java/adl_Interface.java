





import java.util.List;
import java.util.ArrayList;

public class adl_Interface extends NamedElement {






    private adl_Binding adl_binding;




    private List<adl_Binding> adl_bindings;




    private adl_Binding adl_binding;


    public adl_Interface(
    ) {
        super(
        );
        this.adl_bindings = new ArrayList<>();
    }

    public adl_Interface(
        ArrayList<adl_Binding> adl_bindings    ) {
        this.adl_bindings = adl_bindings;
    }


    public adl_Binding getAdl_binding() {
        return adl_binding;
    }

    public void setAdl_binding(adl_Binding adl_binding) {
        this.adl_binding = adl_binding;
    }
    public List<adl_Binding> getAdl_bindings() {
        return adl_bindings;
    }

    public void addAdl_binding(Adl_binding adl_binding) {
        this.adl_bindings.add(adl_binding);
    }
    public adl_Binding getAdl_binding() {
        return adl_binding;
    }

    public void setAdl_binding(adl_Binding adl_binding) {
        this.adl_binding = adl_binding;
    }

}
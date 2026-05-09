





import java.util.List;
import java.util.ArrayList;

public class atl_n_ocl_ATL_OutPatternElement extends PatternElement {






    private InPatternElement inpatternelement;




    private List<Binding> bindings;




    private OclModel oclmodel;


    public atl_n_ocl_ATL_OutPatternElement(
    ) {
        super(
        );
        this.bindings = new ArrayList<>();
    }

    public atl_n_ocl_ATL_OutPatternElement(
        ArrayList<Binding> bindings    ) {
        this.bindings = bindings;
    }


    public InPatternElement getInpatternelement() {
        return inpatternelement;
    }

    public void setInpatternelement(InPatternElement inpatternelement) {
        this.inpatternelement = inpatternelement;
    }
    public List<Binding> getBindings() {
        return bindings;
    }

    public void addBinding(Binding binding) {
        this.bindings.add(binding);
    }
    public OclModel getOclmodel() {
        return oclmodel;
    }

    public void setOclmodel(OclModel oclmodel) {
        this.oclmodel = oclmodel;
    }

}
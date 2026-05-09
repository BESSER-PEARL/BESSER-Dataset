





import java.util.List;
import java.util.ArrayList;

public class ATL_OutPatternElement extends PatternElement {






    private OclModel oclmodel;




    private OutPattern outpattern;




    private List<Binding> bindings;




    private InPatternElement inpatternelement;


    public ATL_OutPatternElement(
    ) {
        super(
        );
        this.bindings = new ArrayList<>();
    }

    public ATL_OutPatternElement(
        ArrayList<Binding> bindings    ) {
        this.bindings = bindings;
    }


    public OclModel getOclmodel() {
        return oclmodel;
    }

    public void setOclmodel(OclModel oclmodel) {
        this.oclmodel = oclmodel;
    }
    public OutPattern getOutpattern() {
        return outpattern;
    }

    public void setOutpattern(OutPattern outpattern) {
        this.outpattern = outpattern;
    }
    public List<Binding> getBindings() {
        return bindings;
    }

    public void addBinding(Binding binding) {
        this.bindings.add(binding);
    }
    public InPatternElement getInpatternelement() {
        return inpatternelement;
    }

    public void setInpatternelement(InPatternElement inpatternelement) {
        this.inpatternelement = inpatternelement;
    }

}






import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Property extends StructuralFeature {

    private boolean derived;
    private boolean composite;
    private boolean derivedUnion;
    private String aggregation;





    private Kernel_Property kernel_property;




    private Kernel_Association kernel_association;




    private Kernel_Association kernel_association;


    public fUML_Kernel_Property(
        boolean derived,        boolean composite,        boolean derivedUnion,        String aggregation    ) {
        super(
        );
        this.derived = derived;
        this.composite = composite;
        this.derivedUnion = derivedUnion;
        this.aggregation = aggregation;
    }


    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public boolean getComposite() {
        return composite;
    }

    public void setComposite(boolean composite) {
        this.composite = composite;
    }
    public boolean getDerivedunion() {
        return derivedUnion;
    }

    public void setDerivedunion(boolean derivedUnion) {
        this.derivedUnion = derivedUnion;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }

    public Kernel_Property getKernel_property() {
        return kernel_property;
    }

    public void setKernel_property(Kernel_Property kernel_property) {
        this.kernel_property = kernel_property;
    }
    public Kernel_Association getKernel_association() {
        return kernel_association;
    }

    public void setKernel_association(Kernel_Association kernel_association) {
        this.kernel_association = kernel_association;
    }
    public Kernel_Association getKernel_association() {
        return kernel_association;
    }

    public void setKernel_association(Kernel_Association kernel_association) {
        this.kernel_association = kernel_association;
    }

}
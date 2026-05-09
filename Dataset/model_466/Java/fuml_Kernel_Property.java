





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_Property extends StructuralFeature {

    private String aggregation;
    private boolean derived;
    private boolean derivedUnion;
    private boolean composite;





    private Kernel_Property kernel_property;




    private Kernel_Association kernel_association;




    private Kernel_Association kernel_association;


    public fuml_Kernel_Property(
        String aggregation,        boolean derived,        boolean derivedUnion,        boolean composite    ) {
        super(
        );
        this.aggregation = aggregation;
        this.derived = derived;
        this.derivedUnion = derivedUnion;
        this.composite = composite;
    }


    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public boolean getDerivedunion() {
        return derivedUnion;
    }

    public void setDerivedunion(boolean derivedUnion) {
        this.derivedUnion = derivedUnion;
    }
    public boolean getComposite() {
        return composite;
    }

    public void setComposite(boolean composite) {
        this.composite = composite;
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
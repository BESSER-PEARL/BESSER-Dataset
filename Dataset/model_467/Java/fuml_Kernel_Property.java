





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_Property extends StructuralFeature {

    private boolean derivedUnion;
    private boolean composite;
    private boolean derived;
    private String aggregation;





    private Kernel_Property kernel_property;


    public fuml_Kernel_Property(
        boolean derivedUnion,        boolean composite,        boolean derived,        String aggregation    ) {
        super(
        );
        this.derivedUnion = derivedUnion;
        this.composite = composite;
        this.derived = derived;
        this.aggregation = aggregation;
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
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
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

}
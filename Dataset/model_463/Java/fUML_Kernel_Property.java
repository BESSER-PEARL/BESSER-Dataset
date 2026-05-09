





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Property extends StructuralFeature {

    private boolean derived;
    private boolean derivedUnion;
    private boolean composite;
    private String aggregation;



    public fUML_Kernel_Property(
        boolean derived,        boolean derivedUnion,        boolean composite,        String aggregation    ) {
        super(
        );
        this.derived = derived;
        this.derivedUnion = derivedUnion;
        this.composite = composite;
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
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }


}
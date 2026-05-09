





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_Property extends StructuralFeature {

    private boolean derived;
    private boolean derivedUnion;
    private String aggregation;
    private boolean composite;





    private Kernel_Property kernel_property;




    private Kernel_DataType kernel_datatype;


    public fuml_Kernel_Property(
        boolean derived,        boolean derivedUnion,        String aggregation,        boolean composite    ) {
        super(
        );
        this.derived = derived;
        this.derivedUnion = derivedUnion;
        this.aggregation = aggregation;
        this.composite = composite;
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
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
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
    public Kernel_DataType getKernel_datatype() {
        return kernel_datatype;
    }

    public void setKernel_datatype(Kernel_DataType kernel_datatype) {
        this.kernel_datatype = kernel_datatype;
    }

}
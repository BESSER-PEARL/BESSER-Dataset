





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Property extends StructuralFeature {

    private boolean derived;
    private String aggregation;
    private boolean derivedUnion;
    private boolean composite;





    private Kernel_Association kernel_association;




    private Kernel_Property kernel_property;




    private Kernel_Association kernel_association;




    private Kernel_Class kernel_class;




    private Kernel_DataType kernel_datatype;


    public fUML_Kernel_Property(
        boolean derived,        String aggregation,        boolean derivedUnion,        boolean composite    ) {
        super(
        );
        this.derived = derived;
        this.aggregation = aggregation;
        this.derivedUnion = derivedUnion;
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

    public Kernel_Association getKernel_association() {
        return kernel_association;
    }

    public void setKernel_association(Kernel_Association kernel_association) {
        this.kernel_association = kernel_association;
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
    public Kernel_Class getKernel_class() {
        return kernel_class;
    }

    public void setKernel_class(Kernel_Class kernel_class) {
        this.kernel_class = kernel_class;
    }
    public Kernel_DataType getKernel_datatype() {
        return kernel_datatype;
    }

    public void setKernel_datatype(Kernel_DataType kernel_datatype) {
        this.kernel_datatype = kernel_datatype;
    }

}
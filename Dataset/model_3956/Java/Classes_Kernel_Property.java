





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_Property extends StructuralFeature {

    private String default;
    private boolean isDerived;
    private boolean isComposite;
    private String aggregation;
    private boolean isID;
    private boolean isDerivedUnion;





    private ValueSpecification valuespecification;


    public Classes_Kernel_Property(
        String default,        boolean isDerived,        boolean isComposite,        String aggregation,        boolean isID,        boolean isDerivedUnion    ) {
        super(
        );
        this.default = default;
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.aggregation = aggregation;
        this.isID = isID;
        this.isDerivedUnion = isDerivedUnion;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public boolean getIsid() {
        return isID;
    }

    public void setIsid(boolean isID) {
        this.isID = isID;
    }
    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }

    public ValueSpecification getValuespecification() {
        return valuespecification;
    }

    public void setValuespecification(ValueSpecification valuespecification) {
        this.valuespecification = valuespecification;
    }

}
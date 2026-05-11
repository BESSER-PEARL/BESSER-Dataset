





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_ETypedElement extends ENamedElement {

    private int lowerBound;
    private boolean ordered;
    private int upperBound;
    private boolean unique;
    private boolean many;
    private boolean required;





    private RefinementsEcore_EClassifier refinementsecore_eclassifier;


    public RefinementsEcore_ETypedElement(
        int lowerBound,        boolean ordered,        int upperBound,        boolean unique,        boolean many,        boolean required    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.ordered = ordered;
        this.upperBound = upperBound;
        this.unique = unique;
        this.many = many;
        this.required = required;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }

    public RefinementsEcore_EClassifier getRefinementsecore_eclassifier() {
        return refinementsecore_eclassifier;
    }

    public void setRefinementsecore_eclassifier(RefinementsEcore_EClassifier refinementsecore_eclassifier) {
        this.refinementsecore_eclassifier = refinementsecore_eclassifier;
    }

}






import java.util.List;
import java.util.ArrayList;

public class ecorer_ETypedElement extends ENamedElement {

    private boolean ordered;
    private int upperBound;
    private boolean many;
    private boolean required;
    private boolean unique;
    private int lowerBound;





    private ecorer_EClassifier ecorer_eclassifier;


    public ecorer_ETypedElement(
        boolean ordered,        int upperBound,        boolean many,        boolean required,        boolean unique,        int lowerBound    ) {
        super(
        );
        this.ordered = ordered;
        this.upperBound = upperBound;
        this.many = many;
        this.required = required;
        this.unique = unique;
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
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }

    public ecorer_EClassifier getEcorer_eclassifier() {
        return ecorer_eclassifier;
    }

    public void setEcorer_eclassifier(ecorer_EClassifier ecorer_eclassifier) {
        this.ecorer_eclassifier = ecorer_eclassifier;
    }

}
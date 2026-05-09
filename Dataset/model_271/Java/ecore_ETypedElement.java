





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private boolean many;
    private boolean unique;
    private int lowerBound;
    private boolean ordered;
    private int upperBound;
    private boolean required;





    private ecore_EClassifier ecore_eclassifier;


    public ecore_ETypedElement(
        boolean many,        boolean unique,        int lowerBound,        boolean ordered,        int upperBound,        boolean required    ) {
        super(
        );
        this.many = many;
        this.unique = unique;
        this.lowerBound = lowerBound;
        this.ordered = ordered;
        this.upperBound = upperBound;
        this.required = required;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
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
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }

    public ecore_EClassifier getEcore_eclassifier() {
        return ecore_eclassifier;
    }

    public void setEcore_eclassifier(ecore_EClassifier ecore_eclassifier) {
        this.ecore_eclassifier = ecore_eclassifier;
    }

}
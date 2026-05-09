





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private boolean required;
    private boolean many;
    private boolean unique;
    private int upperBound;
    private int lowerBound;
    private boolean ordered;





    private ecore_EClassifier ecore_eclassifier;


    public ecore_ETypedElement(
        boolean required,        boolean many,        boolean unique,        int upperBound,        int lowerBound,        boolean ordered    ) {
        super(
        );
        this.required = required;
        this.many = many;
        this.unique = unique;
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
        this.ordered = ordered;
    }


    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
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
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
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

    public ecore_EClassifier getEcore_eclassifier() {
        return ecore_eclassifier;
    }

    public void setEcore_eclassifier(ecore_EClassifier ecore_eclassifier) {
        this.ecore_eclassifier = ecore_eclassifier;
    }

}
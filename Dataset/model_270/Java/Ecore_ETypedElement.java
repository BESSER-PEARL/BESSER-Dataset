





import java.util.List;
import java.util.ArrayList;

public class Ecore_ETypedElement extends ENamedElement {

    private boolean unique;
    private boolean ordered;
    private boolean required;
    private boolean many;
    private int lowerBound;
    private int upperBound;





    private Ecore_EClassifier ecore_eclassifier;


    public Ecore_ETypedElement(
        boolean unique,        boolean ordered,        boolean required,        boolean many,        int lowerBound,        int upperBound    ) {
        super(
        );
        this.unique = unique;
        this.ordered = ordered;
        this.required = required;
        this.many = many;
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
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
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }

    public Ecore_EClassifier getEcore_eclassifier() {
        return ecore_eclassifier;
    }

    public void setEcore_eclassifier(Ecore_EClassifier ecore_eclassifier) {
        this.ecore_eclassifier = ecore_eclassifier;
    }

}
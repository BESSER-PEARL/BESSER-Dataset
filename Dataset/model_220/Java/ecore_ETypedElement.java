





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private boolean many;
    private boolean required;
    private int upperBound;
    private boolean ordered;
    private int lowerBound;
    private boolean unique;





    private ecore_EClassifier ecore_eclassifier;




    private ecore_EGenericType ecore_egenerictype;


    public ecore_ETypedElement(
        boolean many,        boolean required,        int upperBound,        boolean ordered,        int lowerBound,        boolean unique    ) {
        super(
        );
        this.many = many;
        this.required = required;
        this.upperBound = upperBound;
        this.ordered = ordered;
        this.lowerBound = lowerBound;
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
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }

    public ecore_EClassifier getEcore_eclassifier() {
        return ecore_eclassifier;
    }

    public void setEcore_eclassifier(ecore_EClassifier ecore_eclassifier) {
        this.ecore_eclassifier = ecore_eclassifier;
    }
    public ecore_EGenericType getEcore_egenerictype() {
        return ecore_egenerictype;
    }

    public void setEcore_egenerictype(ecore_EGenericType ecore_egenerictype) {
        this.ecore_egenerictype = ecore_egenerictype;
    }

}
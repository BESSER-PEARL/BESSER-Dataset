





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private int upperBound;
    private boolean unique;
    private int lowerBound;
    private boolean many;
    private boolean required;
    private boolean ordered;





    private ecore_EClassifier ecore_eclassifier;




    private ecore_EGenericType ecore_egenerictype;


    public ecore_ETypedElement(
        int upperBound,        boolean unique,        int lowerBound,        boolean many,        boolean required,        boolean ordered    ) {
        super(
        );
        this.upperBound = upperBound;
        this.unique = unique;
        this.lowerBound = lowerBound;
        this.many = many;
        this.required = required;
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
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
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
    public ecore_EGenericType getEcore_egenerictype() {
        return ecore_egenerictype;
    }

    public void setEcore_egenerictype(ecore_EGenericType ecore_egenerictype) {
        this.ecore_egenerictype = ecore_egenerictype;
    }

}
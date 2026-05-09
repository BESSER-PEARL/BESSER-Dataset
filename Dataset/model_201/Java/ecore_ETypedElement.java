





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private boolean ordered;
    private boolean many;
    private int upperBound;
    private int lowerBound;
    private boolean required;
    private boolean unique;





    private ecore_EClassifier ecore_eclassifier;




    private ecore_EGenericType ecore_egenerictype;


    public ecore_ETypedElement(
        boolean ordered,        boolean many,        int upperBound,        int lowerBound,        boolean required,        boolean unique    ) {
        super(
        );
        this.ordered = ordered;
        this.many = many;
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
        this.required = required;
        this.unique = unique;
    }


    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
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
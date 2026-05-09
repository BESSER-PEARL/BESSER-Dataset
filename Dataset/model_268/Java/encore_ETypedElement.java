





import java.util.List;
import java.util.ArrayList;

public class encore_ETypedElement extends ENamedElement {

    private boolean ordered;
    private boolean many;
    private int upperBound;
    private boolean unique;
    private int lowerBound;
    private boolean required;





    private encore_EGenericType encore_egenerictype;




    private encore_EClassifier encore_eclassifier;


    public encore_ETypedElement(
        boolean ordered,        boolean many,        int upperBound,        boolean unique,        int lowerBound,        boolean required    ) {
        super(
        );
        this.ordered = ordered;
        this.many = many;
        this.upperBound = upperBound;
        this.unique = unique;
        this.lowerBound = lowerBound;
        this.required = required;
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
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }

    public encore_EGenericType getEncore_egenerictype() {
        return encore_egenerictype;
    }

    public void setEncore_egenerictype(encore_EGenericType encore_egenerictype) {
        this.encore_egenerictype = encore_egenerictype;
    }
    public encore_EClassifier getEncore_eclassifier() {
        return encore_eclassifier;
    }

    public void setEncore_eclassifier(encore_EClassifier encore_eclassifier) {
        this.encore_eclassifier = encore_eclassifier;
    }

}
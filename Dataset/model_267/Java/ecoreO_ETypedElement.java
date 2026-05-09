





import java.util.List;
import java.util.ArrayList;

public class ecoreO_ETypedElement extends ENamedElement {

    private boolean unique;
    private int upperBound;
    private boolean many;
    private boolean required;
    private boolean ordered;
    private int lowerBound;





    private ecoreO_EClassifier ecoreo_eclassifier;




    private ecoreO_EGenericType ecoreo_egenerictype;


    public ecoreO_ETypedElement(
        boolean unique,        int upperBound,        boolean many,        boolean required,        boolean ordered,        int lowerBound    ) {
        super(
        );
        this.unique = unique;
        this.upperBound = upperBound;
        this.many = many;
        this.required = required;
        this.ordered = ordered;
        this.lowerBound = lowerBound;
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
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }

    public ecoreO_EClassifier getEcoreo_eclassifier() {
        return ecoreo_eclassifier;
    }

    public void setEcoreo_eclassifier(ecoreO_EClassifier ecoreo_eclassifier) {
        this.ecoreo_eclassifier = ecoreo_eclassifier;
    }
    public ecoreO_EGenericType getEcoreo_egenerictype() {
        return ecoreo_egenerictype;
    }

    public void setEcoreo_egenerictype(ecoreO_EGenericType ecoreo_egenerictype) {
        this.ecoreo_egenerictype = ecoreo_egenerictype;
    }

}
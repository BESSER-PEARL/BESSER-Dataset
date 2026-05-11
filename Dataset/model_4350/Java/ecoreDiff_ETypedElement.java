





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ETypedElement extends ENamedElement {

    private boolean ordered;
    private int upperBound;
    private boolean unique;
    private boolean required;
    private int lowerBound;
    private boolean many;





    private ecoreDiff_EGenericType ecorediff_egenerictype;




    private ecoreDiff_EObject ecorediff_eobject;


    public ecoreDiff_ETypedElement(
        boolean ordered,        int upperBound,        boolean unique,        boolean required,        int lowerBound,        boolean many    ) {
        super(
        );
        this.ordered = ordered;
        this.upperBound = upperBound;
        this.unique = unique;
        this.required = required;
        this.lowerBound = lowerBound;
        this.many = many;
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
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
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

    public ecoreDiff_EGenericType getEcorediff_egenerictype() {
        return ecorediff_egenerictype;
    }

    public void setEcorediff_egenerictype(ecoreDiff_EGenericType ecorediff_egenerictype) {
        this.ecorediff_egenerictype = ecorediff_egenerictype;
    }
    public ecoreDiff_EObject getEcorediff_eobject() {
        return ecorediff_eobject;
    }

    public void setEcorediff_eobject(ecoreDiff_EObject ecorediff_eobject) {
        this.ecorediff_eobject = ecorediff_eobject;
    }

}
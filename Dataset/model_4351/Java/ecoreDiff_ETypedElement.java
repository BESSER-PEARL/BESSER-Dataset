





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ETypedElement extends ENamedElement {

    private boolean many;
    private boolean ordered;
    private int lowerBound;
    private String required;
    private int upperBound;
    private boolean unique;





    private ecoreDiff_EGenericType ecorediff_egenerictype;


    public ecoreDiff_ETypedElement(
        boolean many,        boolean ordered,        int lowerBound,        String required,        int upperBound,        boolean unique    ) {
        super(
        );
        this.many = many;
        this.ordered = ordered;
        this.lowerBound = lowerBound;
        this.required = required;
        this.upperBound = upperBound;
        this.unique = unique;
    }


    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
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
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
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

    public ecoreDiff_EGenericType getEcorediff_egenerictype() {
        return ecorediff_egenerictype;
    }

    public void setEcorediff_egenerictype(ecoreDiff_EGenericType ecorediff_egenerictype) {
        this.ecorediff_egenerictype = ecorediff_egenerictype;
    }

}
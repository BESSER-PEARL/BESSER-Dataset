





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private boolean required;
    private int upperBound;
    private int lowerBound;
    private boolean ordered;
    private boolean unique;
    private boolean many;



    public ecore_ETypedElement(
        boolean required,        int upperBound,        int lowerBound,        boolean ordered,        boolean unique,        boolean many    ) {
        super(
        );
        this.required = required;
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
        this.ordered = ordered;
        this.unique = unique;
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
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }


}
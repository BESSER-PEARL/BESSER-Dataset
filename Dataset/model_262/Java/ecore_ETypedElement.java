





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private boolean unique;
    private boolean many;
    private int lowerBound;
    private boolean ordered;
    private boolean required;
    private int upperBound;



    public ecore_ETypedElement(
        boolean unique,        boolean many,        int lowerBound,        boolean ordered,        boolean required,        int upperBound    ) {
        super(
        );
        this.unique = unique;
        this.many = many;
        this.lowerBound = lowerBound;
        this.ordered = ordered;
        this.required = required;
        this.upperBound = upperBound;
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


}
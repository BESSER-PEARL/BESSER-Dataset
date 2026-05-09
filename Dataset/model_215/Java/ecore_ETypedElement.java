





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypedElement extends ENamedElement {

    private boolean required;
    private boolean many;
    private int lowerBound;
    private boolean ordered;
    private int upperBound;
    private boolean unique;



    public ecore_ETypedElement(
        boolean required,        boolean many,        int lowerBound,        boolean ordered,        int upperBound,        boolean unique    ) {
        super(
        );
        this.required = required;
        this.many = many;
        this.lowerBound = lowerBound;
        this.ordered = ordered;
        this.upperBound = upperBound;
        this.unique = unique;
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


}






import java.util.List;
import java.util.ArrayList;

public class javaless_ETypedElement extends ENamedElement {

    private boolean many;
    private boolean ordered;
    private int upperBound;
    private boolean required;
    private boolean unique;
    private int lowerBound;





    private javaless_EClassifier javaless_eclassifier;


    public javaless_ETypedElement(
        boolean many,        boolean ordered,        int upperBound,        boolean required,        boolean unique,        int lowerBound    ) {
        super(
        );
        this.many = many;
        this.ordered = ordered;
        this.upperBound = upperBound;
        this.required = required;
        this.unique = unique;
        this.lowerBound = lowerBound;
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
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
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
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }

    public javaless_EClassifier getJavaless_eclassifier() {
        return javaless_eclassifier;
    }

    public void setJavaless_eclassifier(javaless_EClassifier javaless_eclassifier) {
        this.javaless_eclassifier = javaless_eclassifier;
    }

}
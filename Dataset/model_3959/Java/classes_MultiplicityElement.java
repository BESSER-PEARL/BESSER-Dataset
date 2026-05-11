





import java.util.List;
import java.util.ArrayList;

public class classes_MultiplicityElement extends Element {

    private boolean unique;
    private int lower;
    private int upper;
    private boolean ordered;





    private classes_ValueSpecification classes_valuespecification;




    private classes_ValueSpecification classes_valuespecification;


    public classes_MultiplicityElement(
        boolean unique,        int lower,        int upper,        boolean ordered    ) {
        super(
        );
        this.unique = unique;
        this.lower = lower;
        this.upper = upper;
        this.ordered = ordered;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }

    public classes_ValueSpecification getClasses_valuespecification() {
        return classes_valuespecification;
    }

    public void setClasses_valuespecification(classes_ValueSpecification classes_valuespecification) {
        this.classes_valuespecification = classes_valuespecification;
    }
    public classes_ValueSpecification getClasses_valuespecification() {
        return classes_valuespecification;
    }

    public void setClasses_valuespecification(classes_ValueSpecification classes_valuespecification) {
        this.classes_valuespecification = classes_valuespecification;
    }

}
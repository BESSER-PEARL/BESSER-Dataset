





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_MultiplicityElement extends Element {

    private int lower;
    private boolean ordered;
    private boolean unique;
    private int upper;



    public fuml_Kernel_MultiplicityElement(
        int lower,        boolean ordered,        boolean unique,        int upper    ) {
        super(
        );
        this.lower = lower;
        this.ordered = ordered;
        this.unique = unique;
        this.upper = upper;
    }


    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
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
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }


}
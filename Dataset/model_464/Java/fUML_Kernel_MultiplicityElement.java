





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_MultiplicityElement extends Element {

    private boolean ordered;
    private int lower;
    private int upper;
    private boolean unique;



    public fUML_Kernel_MultiplicityElement(
        boolean ordered,        int lower,        int upper,        boolean unique    ) {
        super(
        );
        this.ordered = ordered;
        this.lower = lower;
        this.upper = upper;
        this.unique = unique;
    }


    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
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
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }


}
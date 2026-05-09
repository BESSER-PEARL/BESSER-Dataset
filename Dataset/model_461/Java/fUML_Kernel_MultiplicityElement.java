





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_MultiplicityElement extends Element {

    private int upper;
    private boolean ordered;
    private boolean unique;
    private int lower;



    public fUML_Kernel_MultiplicityElement(
        int upper,        boolean ordered,        boolean unique,        int lower    ) {
        super(
        );
        this.upper = upper;
        this.ordered = ordered;
        this.unique = unique;
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


}
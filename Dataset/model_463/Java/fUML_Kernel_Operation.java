





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Operation extends BehavioralFeature {

    private boolean unique;
    private boolean ordered;
    private boolean query;
    private int lower;
    private int upper;





    private Kernel_Class kernel_class;


    public fUML_Kernel_Operation(
        boolean unique,        boolean ordered,        boolean query,        int lower,        int upper    ) {
        super(
        );
        this.unique = unique;
        this.ordered = ordered;
        this.query = query;
        this.lower = lower;
        this.upper = upper;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public boolean getQuery() {
        return query;
    }

    public void setQuery(boolean query) {
        this.query = query;
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

    public Kernel_Class getKernel_class() {
        return kernel_class;
    }

    public void setKernel_class(Kernel_Class kernel_class) {
        this.kernel_class = kernel_class;
    }

}






import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_Operation extends BehavioralFeature {

    private int upper;
    private boolean ordered;
    private boolean unique;
    private boolean query;
    private int lower;





    private Kernel_Type kernel_type;


    public fuml_Kernel_Operation(
        int upper,        boolean ordered,        boolean unique,        boolean query,        int lower    ) {
        super(
        );
        this.upper = upper;
        this.ordered = ordered;
        this.unique = unique;
        this.query = query;
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

    public Kernel_Type getKernel_type() {
        return kernel_type;
    }

    public void setKernel_type(Kernel_Type kernel_type) {
        this.kernel_type = kernel_type;
    }

}
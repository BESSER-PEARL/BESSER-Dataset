





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Operation extends BehavioralFeature {

    private boolean ordered;
    private int upper;
    private boolean query;
    private int lower;
    private boolean unique;



    public fUML_Kernel_Operation(
        boolean ordered,        int upper,        boolean query,        int lower,        boolean unique    ) {
        super(
        );
        this.ordered = ordered;
        this.upper = upper;
        this.query = query;
        this.lower = lower;
        this.unique = unique;
    }


    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
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
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }


}
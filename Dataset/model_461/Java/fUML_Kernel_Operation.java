





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Operation extends BehavioralFeature {

    private boolean unique;
    private boolean query;
    private int upper;
    private boolean ordered;
    private int lower;



    public fUML_Kernel_Operation(
        boolean unique,        boolean query,        int upper,        boolean ordered,        int lower    ) {
        super(
        );
        this.unique = unique;
        this.query = query;
        this.upper = upper;
        this.ordered = ordered;
        this.lower = lower;
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
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }


}
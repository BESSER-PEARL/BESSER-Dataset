





import java.util.List;
import java.util.ArrayList;

public class fUML_Kernel_Operation extends BehavioralFeature {

    private boolean ordered;
    private int upper;
    private int lower;
    private boolean unique;
    private boolean query;



    public fUML_Kernel_Operation(
        boolean ordered,        int upper,        int lower,        boolean unique,        boolean query    ) {
        super(
        );
        this.ordered = ordered;
        this.upper = upper;
        this.lower = lower;
        this.unique = unique;
        this.query = query;
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
    public boolean getQuery() {
        return query;
    }

    public void setQuery(boolean query) {
        this.query = query;
    }


}
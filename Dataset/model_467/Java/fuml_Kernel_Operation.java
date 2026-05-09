





import java.util.List;
import java.util.ArrayList;

public class fuml_Kernel_Operation extends BehavioralFeature {

    private boolean query;
    private boolean ordered;
    private int lower;
    private boolean unique;
    private int upper;



    public fuml_Kernel_Operation(
        boolean query,        boolean ordered,        int lower,        boolean unique,        int upper    ) {
        super(
        );
        this.query = query;
        this.ordered = ordered;
        this.lower = lower;
        this.unique = unique;
        this.upper = upper;
    }


    public boolean getQuery() {
        return query;
    }

    public void setQuery(boolean query) {
        this.query = query;
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
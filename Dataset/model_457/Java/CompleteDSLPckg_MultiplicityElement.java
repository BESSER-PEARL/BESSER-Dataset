





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_MultiplicityElement extends Element {

    private boolean isUnique;
    private int upper;
    private int lower;
    private boolean isOrdered;



    public CompleteDSLPckg_MultiplicityElement(
        boolean isUnique,        int upper,        int lower,        boolean isOrdered    ) {
        super(
        );
        this.isUnique = isUnique;
        this.upper = upper;
        this.lower = lower;
        this.isOrdered = isOrdered;
    }


    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
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
    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }


}
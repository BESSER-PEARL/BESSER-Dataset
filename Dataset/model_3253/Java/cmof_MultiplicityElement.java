





import java.util.List;
import java.util.ArrayList;

public class cmof_MultiplicityElement extends Element {

    private int upper;
    private boolean isOrdered;
    private int lower;
    private boolean isUnique;



    public cmof_MultiplicityElement(
        int upper,        boolean isOrdered,        int lower,        boolean isUnique    ) {
        super(
        );
        this.upper = upper;
        this.isOrdered = isOrdered;
        this.lower = lower;
        this.isUnique = isUnique;
    }


    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
    }


}
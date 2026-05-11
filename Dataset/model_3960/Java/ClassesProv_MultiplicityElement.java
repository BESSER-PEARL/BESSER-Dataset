





import java.util.List;
import java.util.ArrayList;

public class ClassesProv_MultiplicityElement extends Element {

    private boolean isUnique;
    private int lower;
    private int upper;
    private boolean isOrdered;



    public ClassesProv_MultiplicityElement(
        boolean isUnique,        int lower,        int upper,        boolean isOrdered    ) {
        super(
        );
        this.isUnique = isUnique;
        this.lower = lower;
        this.upper = upper;
        this.isOrdered = isOrdered;
    }


    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
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
    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }


}
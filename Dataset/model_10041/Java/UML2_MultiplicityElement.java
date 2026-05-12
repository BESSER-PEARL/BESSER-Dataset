





import java.util.List;
import java.util.ArrayList;

public class UML2_MultiplicityElement extends Element {

    private int lower;
    private boolean isUnique;
    private String upper;
    private boolean isOrdered;



    public UML2_MultiplicityElement(
        int lower,        boolean isUnique,        String upper,        boolean isOrdered    ) {
        super(
        );
        this.lower = lower;
        this.isUnique = isUnique;
        this.upper = upper;
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
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }


}
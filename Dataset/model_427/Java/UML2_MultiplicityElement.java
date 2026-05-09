





import java.util.List;
import java.util.ArrayList;

public class UML2_MultiplicityElement extends Element {

    private String upper;
    private boolean isUnique;
    private int lower;
    private boolean isOrdered;



    public UML2_MultiplicityElement(
        String upper,        boolean isUnique,        int lower,        boolean isOrdered    ) {
        super(
        );
        this.upper = upper;
        this.isUnique = isUnique;
        this.lower = lower;
        this.isOrdered = isOrdered;
    }


    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
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
    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }


}
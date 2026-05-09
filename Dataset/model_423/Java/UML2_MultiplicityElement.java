





import java.util.List;
import java.util.ArrayList;

public class UML2_MultiplicityElement extends Element {

    private boolean isUnique;
    private int lower;
    private String upper;
    private boolean isOrdered;



    public UML2_MultiplicityElement(
        boolean isUnique,        int lower,        String upper,        boolean isOrdered    ) {
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
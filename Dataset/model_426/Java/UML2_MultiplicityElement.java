





import java.util.List;
import java.util.ArrayList;

public class UML2_MultiplicityElement extends Element {

    private int lower;
    private String upper;
    private boolean isOrdered;
    private boolean isUnique;



    public UML2_MultiplicityElement(
        int lower,        String upper,        boolean isOrdered,        boolean isUnique    ) {
        super(
        );
        this.lower = lower;
        this.upper = upper;
        this.isOrdered = isOrdered;
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
    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
    }


}
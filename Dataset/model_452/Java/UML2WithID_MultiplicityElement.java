





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_MultiplicityElement extends Element {

    private String upper;
    private int lower;
    private boolean isOrdered;
    private boolean isUnique;



    public UML2WithID_MultiplicityElement(
        String upper,        int lower,        boolean isOrdered,        boolean isUnique    ) {
        super(
        );
        this.upper = upper;
        this.lower = lower;
        this.isOrdered = isOrdered;
        this.isUnique = isUnique;
    }


    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
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
    public boolean getIsunique() {
        return isUnique;
    }

    public void setIsunique(boolean isUnique) {
        this.isUnique = isUnique;
    }


}
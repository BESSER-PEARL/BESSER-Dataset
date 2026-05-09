





import java.util.List;
import java.util.ArrayList;

public class UML2_MultiplicityElement extends Element {

    private boolean isOrdered;
    private boolean isUnique;
    private String upper;
    private int lower;



    public UML2_MultiplicityElement(
        boolean isOrdered,        boolean isUnique,        String upper,        int lower    ) {
        super(
        );
        this.isOrdered = isOrdered;
        this.isUnique = isUnique;
        this.upper = upper;
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


}
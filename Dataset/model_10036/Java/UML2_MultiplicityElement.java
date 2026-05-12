





import java.util.List;
import java.util.ArrayList;

public class UML2_MultiplicityElement extends Element {

    private int lower;
    private boolean isUnique;
    private boolean isOrdered;
    private String upper;



    public UML2_MultiplicityElement(
        int lower,        boolean isUnique,        boolean isOrdered,        String upper    ) {
        super(
        );
        this.lower = lower;
        this.isUnique = isUnique;
        this.isOrdered = isOrdered;
        this.upper = upper;
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
    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }


}
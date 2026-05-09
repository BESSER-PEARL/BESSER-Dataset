





import java.util.List;
import java.util.ArrayList;

public class UML2_MultiplicityElement extends Element {

    private boolean isUnique;
    private boolean isOrdered;
    private int lower;
    private String upper;



    public UML2_MultiplicityElement(
        boolean isUnique,        boolean isOrdered,        int lower,        String upper    ) {
        super(
        );
        this.isUnique = isUnique;
        this.isOrdered = isOrdered;
        this.lower = lower;
        this.upper = upper;
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


}
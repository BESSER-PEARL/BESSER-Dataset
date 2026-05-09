





import java.util.List;
import java.util.ArrayList;

public class JTL_emof_MultiplicityElement  {

    private int lower;
    private String isOrdered;
    private String isUnique;
    private String upper;



    public JTL_emof_MultiplicityElement(
        int lower,        String isOrdered,        String isUnique,        String upper    ) {
        this.lower = lower;
        this.isOrdered = isOrdered;
        this.isUnique = isUnique;
        this.upper = upper;
    }


    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }
    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }


}
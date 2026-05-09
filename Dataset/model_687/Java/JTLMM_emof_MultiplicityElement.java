





import java.util.List;
import java.util.ArrayList;

public class JTLMM_emof_MultiplicityElement  {

    private String isUnique;
    private String isOrdered;
    private String upper;
    private int lower;



    public JTLMM_emof_MultiplicityElement(
        String isUnique,        String isOrdered,        String upper,        int lower    ) {
        this.isUnique = isUnique;
        this.isOrdered = isOrdered;
        this.upper = upper;
        this.lower = lower;
    }


    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
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
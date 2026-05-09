





import java.util.List;
import java.util.ArrayList;

public class JTLMM_emof_MultiplicityElement  {

    private String upper;
    private int lower;
    private String isUnique;
    private String isOrdered;



    public JTLMM_emof_MultiplicityElement(
        String upper,        int lower,        String isUnique,        String isOrdered    ) {
        this.upper = upper;
        this.lower = lower;
        this.isUnique = isUnique;
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


}
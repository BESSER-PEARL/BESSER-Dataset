





import java.util.List;
import java.util.ArrayList;

public class EMOF_MultiplicityElement  {

    private String upper;
    private String isUnique;
    private String lower;
    private String isOrdered;



    public EMOF_MultiplicityElement(
        String upper,        String isUnique,        String lower,        String isOrdered    ) {
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
    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }


}






import java.util.List;
import java.util.ArrayList;

public class EMOF_MultiplicityElement  {

    private String lower;
    private String isUnique;
    private String isOrdered;
    private String upper;



    public EMOF_MultiplicityElement(
        String lower,        String isUnique,        String isOrdered,        String upper    ) {
        this.lower = lower;
        this.isUnique = isUnique;
        this.isOrdered = isOrdered;
        this.upper = upper;
    }


    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
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


}
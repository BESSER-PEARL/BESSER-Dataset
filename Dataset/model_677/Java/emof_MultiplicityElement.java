





import java.util.List;
import java.util.ArrayList;

public class emof_MultiplicityElement  {

    private String isOrdered;
    private String isUnique;
    private String lower;
    private String upper;



    public emof_MultiplicityElement(
        String isOrdered,        String isUnique,        String lower,        String upper    ) {
        this.isOrdered = isOrdered;
        this.isUnique = isUnique;
        this.lower = lower;
        this.upper = upper;
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
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }


}
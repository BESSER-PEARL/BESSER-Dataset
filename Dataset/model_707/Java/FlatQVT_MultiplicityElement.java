





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_MultiplicityElement  {

    private String isUnique;
    private String lower;
    private String isOrdered;
    private String upper;



    public FlatQVT_MultiplicityElement(
        String isUnique,        String lower,        String isOrdered,        String upper    ) {
        this.isUnique = isUnique;
        this.lower = lower;
        this.isOrdered = isOrdered;
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
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }


}
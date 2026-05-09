





import java.util.List;
import java.util.ArrayList;

public class Janus_emof_MultiplicityElement  {

    private String upper;
    private String isOrdered;
    private int lower;
    private String isUnique;



    public Janus_emof_MultiplicityElement(
        String upper,        String isOrdered,        int lower,        String isUnique    ) {
        this.upper = upper;
        this.isOrdered = isOrdered;
        this.lower = lower;
        this.isUnique = isUnique;
    }


    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
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


}
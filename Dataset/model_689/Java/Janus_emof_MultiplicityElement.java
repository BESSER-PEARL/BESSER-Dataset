





import java.util.List;
import java.util.ArrayList;

public class Janus_emof_MultiplicityElement  {

    private String upper;
    private String isUnique;
    private String isOrdered;
    private int lower;



    public Janus_emof_MultiplicityElement(
        String upper,        String isUnique,        String isOrdered,        int lower    ) {
        this.upper = upper;
        this.isUnique = isUnique;
        this.isOrdered = isOrdered;
        this.lower = lower;
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


}
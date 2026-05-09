





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_MultiplicityElement extends Element {

    private String upper;
    private String isOrdered;
    private String lower;
    private String isUnique;



    public uml3_0_0_MultiplicityElement(
        String upper,        String isOrdered,        String lower,        String isUnique    ) {
        super(
        );
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


}
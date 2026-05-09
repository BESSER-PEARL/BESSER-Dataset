





import java.util.List;
import java.util.ArrayList;

public class org_structure_MultiplicityElement extends TypedElement {

    private String isOrdered;
    private String lower;
    private String upper;
    private String isUnique;



    public org_structure_MultiplicityElement(
        String isOrdered,        String lower,        String upper,        String isUnique    ) {
        super(
        );
        this.isOrdered = isOrdered;
        this.lower = lower;
        this.upper = upper;
        this.isUnique = isUnique;
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


}
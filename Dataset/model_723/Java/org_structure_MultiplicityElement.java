





import java.util.List;
import java.util.ArrayList;

public class org_structure_MultiplicityElement extends TypedElement {

    private String isOrdered;
    private String upper;
    private String lower;
    private String isUnique;



    public org_structure_MultiplicityElement(
        String isOrdered,        String upper,        String lower,        String isUnique    ) {
        super(
        );
        this.isOrdered = isOrdered;
        this.upper = upper;
        this.lower = lower;
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
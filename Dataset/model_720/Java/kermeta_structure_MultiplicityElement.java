





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_MultiplicityElement extends TypedElement {

    private String lower;
    private String upper;
    private String isOrdered;
    private String isUnique;



    public kermeta_structure_MultiplicityElement(
        String lower,        String upper,        String isOrdered,        String isUnique    ) {
        super(
        );
        this.lower = lower;
        this.upper = upper;
        this.isOrdered = isOrdered;
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


}
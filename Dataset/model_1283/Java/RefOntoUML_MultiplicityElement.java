





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_MultiplicityElement extends Element {

    private String isUnique;
    private String upper;
    private String lower;
    private String isOrdered;



    public RefOntoUML_MultiplicityElement(
        String isUnique,        String upper,        String lower,        String isOrdered    ) {
        super(
        );
        this.isUnique = isUnique;
        this.upper = upper;
        this.lower = lower;
        this.isOrdered = isOrdered;
    }


    public String getIsunique() {
        return isUnique;
    }

    public void setIsunique(String isUnique) {
        this.isUnique = isUnique;
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
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }


}
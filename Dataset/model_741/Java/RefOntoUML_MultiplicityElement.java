





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_MultiplicityElement extends Element {

    private String isUnique;
    private String lower;
    private String upper;
    private String isOrdered;



    public RefOntoUML_MultiplicityElement(
        String isUnique,        String lower,        String upper,        String isOrdered    ) {
        super(
        );
        this.isUnique = isUnique;
        this.lower = lower;
        this.upper = upper;
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
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }


}
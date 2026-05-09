





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_MultiplicityElement extends Element {

    private String isUnique;
    private String isOrdered;
    private String lower;
    private String upper;



    public RefOntoUML_MultiplicityElement(
        String isUnique,        String isOrdered,        String lower,        String upper    ) {
        super(
        );
        this.isUnique = isUnique;
        this.isOrdered = isOrdered;
        this.lower = lower;
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
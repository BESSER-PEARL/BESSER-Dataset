





import java.util.List;
import java.util.ArrayList;

public class umlClass_Operation extends NamedElement {

    private String lower;
    private String isQuery;
    private String isUnique;
    private String upper;
    private String isOrdered;



    public umlClass_Operation(
        String lower,        String isQuery,        String isUnique,        String upper,        String isOrdered    ) {
        super(
        );
        this.lower = lower;
        this.isQuery = isQuery;
        this.isUnique = isUnique;
        this.upper = upper;
        this.isOrdered = isOrdered;
    }


    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
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
    public String getIsordered() {
        return isOrdered;
    }

    public void setIsordered(String isOrdered) {
        this.isOrdered = isOrdered;
    }


}






import java.util.List;
import java.util.ArrayList;

public class umlClass_Operation extends NamedElement {

    private String isQuery;
    private String lower;
    private String isOrdered;
    private String isUnique;
    private String upper;



    public umlClass_Operation(
        String isQuery,        String lower,        String isOrdered,        String isUnique,        String upper    ) {
        super(
        );
        this.isQuery = isQuery;
        this.lower = lower;
        this.isOrdered = isOrdered;
        this.isUnique = isUnique;
        this.upper = upper;
    }


    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
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


}
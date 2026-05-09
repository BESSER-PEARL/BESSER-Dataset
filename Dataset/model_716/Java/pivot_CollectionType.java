





import java.util.List;
import java.util.ArrayList;

public class pivot_CollectionType extends DataType {

    private String lower;
    private String isNullFree;
    private String upper;





    private pivot_Type pivot_type;


    public pivot_CollectionType(
        String lower,        String isNullFree,        String upper    ) {
        super(
        );
        this.lower = lower;
        this.isNullFree = isNullFree;
        this.upper = upper;
    }


    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getIsnullfree() {
        return isNullFree;
    }

    public void setIsnullfree(String isNullFree) {
        this.isNullFree = isNullFree;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }

    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }

}
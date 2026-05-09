





import java.util.List;
import java.util.ArrayList;

public class pivot_CollectionType extends DataType {

    private String upper;
    private String isNullFree;
    private String lower;





    private pivot_Type pivot_type;


    public pivot_CollectionType(
        String upper,        String isNullFree,        String lower    ) {
        super(
        );
        this.upper = upper;
        this.isNullFree = isNullFree;
        this.lower = lower;
    }


    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getIsnullfree() {
        return isNullFree;
    }

    public void setIsnullfree(String isNullFree) {
        this.isNullFree = isNullFree;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }

    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }

}
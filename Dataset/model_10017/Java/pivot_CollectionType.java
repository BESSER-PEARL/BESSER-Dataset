





import java.util.List;
import java.util.ArrayList;

public class pivot_CollectionType extends DataType {

    private String lower;
    private String upper;
    private String isNullFree;



    public pivot_CollectionType(
        String lower,        String upper,        String isNullFree    ) {
        super(
        );
        this.lower = lower;
        this.upper = upper;
        this.isNullFree = isNullFree;
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
    public String getIsnullfree() {
        return isNullFree;
    }

    public void setIsnullfree(String isNullFree) {
        this.isNullFree = isNullFree;
    }


}
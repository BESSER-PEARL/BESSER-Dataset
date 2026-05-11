





import java.util.List;
import java.util.ArrayList;

public class ulmDsl2_LookupIntValue  {

    private String description;
    private int value;





    private ulmDsl2_LookupInt ulmdsl2_lookupint;


    public ulmDsl2_LookupIntValue(
        String description,        int value    ) {
        this.description = description;
        this.value = value;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public ulmDsl2_LookupInt getUlmdsl2_lookupint() {
        return ulmdsl2_lookupint;
    }

    public void setUlmdsl2_lookupint(ulmDsl2_LookupInt ulmdsl2_lookupint) {
        this.ulmdsl2_lookupint = ulmdsl2_lookupint;
    }

}
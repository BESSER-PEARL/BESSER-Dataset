





import java.util.List;
import java.util.ArrayList;

public class ulmDsl2_LookupStringValue  {

    private String value;
    private String description;





    private ulmDsl2_LookupString ulmdsl2_lookupstring;


    public ulmDsl2_LookupStringValue(
        String value,        String description    ) {
        this.value = value;
        this.description = description;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public ulmDsl2_LookupString getUlmdsl2_lookupstring() {
        return ulmdsl2_lookupstring;
    }

    public void setUlmdsl2_lookupstring(ulmDsl2_LookupString ulmdsl2_lookupstring) {
        this.ulmdsl2_lookupstring = ulmdsl2_lookupstring;
    }

}
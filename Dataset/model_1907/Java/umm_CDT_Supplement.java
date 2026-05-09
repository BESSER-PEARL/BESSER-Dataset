





import java.util.List;
import java.util.ArrayList;

public class umm_CDT_Supplement extends CDTProperty {

    private String fixedValue;
    private String restriction;
    private String defaultValue;



    public umm_CDT_Supplement(
        String fixedValue,        String restriction,        String defaultValue    ) {
        super(
        );
        this.fixedValue = fixedValue;
        this.restriction = restriction;
        this.defaultValue = defaultValue;
    }


    public String getFixedvalue() {
        return fixedValue;
    }

    public void setFixedvalue(String fixedValue) {
        this.fixedValue = fixedValue;
    }
    public String getRestriction() {
        return restriction;
    }

    public void setRestriction(String restriction) {
        this.restriction = restriction;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}
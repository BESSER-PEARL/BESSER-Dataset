





import java.util.List;
import java.util.ArrayList;

public class umm_Supplement extends BDTProperty {

    private String fixedValue;
    private String defaultValue;
    private String restriction;



    public umm_Supplement(
        String fixedValue,        String defaultValue,        String restriction    ) {
        super(
        );
        this.fixedValue = fixedValue;
        this.defaultValue = defaultValue;
        this.restriction = restriction;
    }


    public String getFixedvalue() {
        return fixedValue;
    }

    public void setFixedvalue(String fixedValue) {
        this.fixedValue = fixedValue;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getRestriction() {
        return restriction;
    }

    public void setRestriction(String restriction) {
        this.restriction = restriction;
    }


}
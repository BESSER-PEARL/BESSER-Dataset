





import java.util.List;
import java.util.ArrayList;

public class umm_BCC extends ACCProperty {

    private String fixedValue;
    private String restriction;



    public umm_BCC(
        String fixedValue,        String restriction    ) {
        super(
        );
        this.fixedValue = fixedValue;
        this.restriction = restriction;
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


}
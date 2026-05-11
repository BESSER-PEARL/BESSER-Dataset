





import java.util.List;
import java.util.ArrayList;

public class aadl2_Property extends BasicProperty, AbstractNamedValue {

    private String emptyListDefault;
    private String inherit;



    public aadl2_Property(
        String emptyListDefault,        String inherit    ) {
        super(
        );
        this.emptyListDefault = emptyListDefault;
        this.inherit = inherit;
    }


    public String getEmptylistdefault() {
        return emptyListDefault;
    }

    public void setEmptylistdefault(String emptyListDefault) {
        this.emptyListDefault = emptyListDefault;
    }
    public String getInherit() {
        return inherit;
    }

    public void setInherit(String inherit) {
        this.inherit = inherit;
    }


}
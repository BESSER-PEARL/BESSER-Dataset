





import java.util.List;
import java.util.ArrayList;

public class website_SelectionParameter extends NamedElement {

    private String defaultValue;
    private boolean optional;



    public website_SelectionParameter(
        String defaultValue,        boolean optional    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.optional = optional;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }


}






import java.util.List;
import java.util.ArrayList;

public class art_type_BasicAttribute extends Attribute {

    private String defaultValue;



    public art_type_BasicAttribute(
        String defaultValue    ) {
        super(
        );
        this.defaultValue = defaultValue;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}
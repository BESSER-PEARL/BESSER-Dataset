





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLBasicDef_StringValue extends ValueType {

    private String value;



    public SpreadsheetMLBasicDef_StringValue(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}
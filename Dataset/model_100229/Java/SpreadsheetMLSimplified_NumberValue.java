





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLSimplified_NumberValue extends ValueType {

    private String value;



    public SpreadsheetMLSimplified_NumberValue(
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
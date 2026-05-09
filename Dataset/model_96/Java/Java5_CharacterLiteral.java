





import java.util.List;
import java.util.ArrayList;

public class Java5_CharacterLiteral extends Expression {

    private String escapedValue;
    private String value;



    public Java5_CharacterLiteral(
        String escapedValue,        String value    ) {
        super(
        );
        this.escapedValue = escapedValue;
        this.value = value;
    }


    public String getEscapedvalue() {
        return escapedValue;
    }

    public void setEscapedvalue(String escapedValue) {
        this.escapedValue = escapedValue;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}
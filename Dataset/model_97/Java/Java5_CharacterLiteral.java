





import java.util.List;
import java.util.ArrayList;

public class Java5_CharacterLiteral extends Expression {

    private String value;
    private String escapedValue;



    public Java5_CharacterLiteral(
        String value,        String escapedValue    ) {
        super(
        );
        this.value = value;
        this.escapedValue = escapedValue;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getEscapedvalue() {
        return escapedValue;
    }

    public void setEscapedvalue(String escapedValue) {
        this.escapedValue = escapedValue;
    }


}
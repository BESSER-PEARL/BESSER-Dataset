





import java.util.List;
import java.util.ArrayList;

public class JDTAST_CharacterLiteral extends Expression {

    private String charValue;
    private String escapedValue;



    public JDTAST_CharacterLiteral(
        String charValue,        String escapedValue    ) {
        super(
        );
        this.charValue = charValue;
        this.escapedValue = escapedValue;
    }


    public String getCharvalue() {
        return charValue;
    }

    public void setCharvalue(String charValue) {
        this.charValue = charValue;
    }
    public String getEscapedvalue() {
        return escapedValue;
    }

    public void setEscapedvalue(String escapedValue) {
        this.escapedValue = escapedValue;
    }


}
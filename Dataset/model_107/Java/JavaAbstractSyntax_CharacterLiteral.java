





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_CharacterLiteral extends Expression {

    private String escapedValue;
    private String charValue;



    public JavaAbstractSyntax_CharacterLiteral(
        String escapedValue,        String charValue    ) {
        super(
        );
        this.escapedValue = escapedValue;
        this.charValue = charValue;
    }


    public String getEscapedvalue() {
        return escapedValue;
    }

    public void setEscapedvalue(String escapedValue) {
        this.escapedValue = escapedValue;
    }
    public String getCharvalue() {
        return charValue;
    }

    public void setCharvalue(String charValue) {
        this.charValue = charValue;
    }


}
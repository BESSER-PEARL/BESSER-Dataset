





import java.util.List;
import java.util.ArrayList;

public class DOM_StringLiteral extends Expression {

    private String literalValue;
    private String escapedValue;



    public DOM_StringLiteral(
        String literalValue,        String escapedValue    ) {
        super(
        );
        this.literalValue = literalValue;
        this.escapedValue = escapedValue;
    }


    public String getLiteralvalue() {
        return literalValue;
    }

    public void setLiteralvalue(String literalValue) {
        this.literalValue = literalValue;
    }
    public String getEscapedvalue() {
        return escapedValue;
    }

    public void setEscapedvalue(String escapedValue) {
        this.escapedValue = escapedValue;
    }


}
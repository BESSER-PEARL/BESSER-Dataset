





import java.util.List;
import java.util.ArrayList;

public class DOM_StringLiteral extends Expression {

    private String escapedValue;
    private String literalValue;



    public DOM_StringLiteral(
        String escapedValue,        String literalValue    ) {
        super(
        );
        this.escapedValue = escapedValue;
        this.literalValue = literalValue;
    }


    public String getEscapedvalue() {
        return escapedValue;
    }

    public void setEscapedvalue(String escapedValue) {
        this.escapedValue = escapedValue;
    }
    public String getLiteralvalue() {
        return literalValue;
    }

    public void setLiteralvalue(String literalValue) {
        this.literalValue = literalValue;
    }


}
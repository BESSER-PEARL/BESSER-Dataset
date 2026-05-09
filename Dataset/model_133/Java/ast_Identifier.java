





import java.util.List;
import java.util.ArrayList;

public class ast_Identifier extends Expression {

    private String escapedValue;
    private String value;
    private String quotedValue;



    public ast_Identifier(
        String escapedValue,        String value,        String quotedValue    ) {
        super(
        );
        this.escapedValue = escapedValue;
        this.value = value;
        this.quotedValue = quotedValue;
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
    public String getQuotedvalue() {
        return quotedValue;
    }

    public void setQuotedvalue(String quotedValue) {
        this.quotedValue = quotedValue;
    }


}
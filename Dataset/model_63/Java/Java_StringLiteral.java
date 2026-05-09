





import java.util.List;
import java.util.ArrayList;

public class Java_StringLiteral extends Expression {

    private String escapedValue;



    public Java_StringLiteral(
        String escapedValue    ) {
        super(
        );
        this.escapedValue = escapedValue;
    }


    public String getEscapedvalue() {
        return escapedValue;
    }

    public void setEscapedvalue(String escapedValue) {
        this.escapedValue = escapedValue;
    }


}
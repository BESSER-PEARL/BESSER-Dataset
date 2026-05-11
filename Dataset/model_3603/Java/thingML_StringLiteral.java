





import java.util.List;
import java.util.ArrayList;

public class thingML_StringLiteral extends Expression {

    private String stringValue;



    public thingML_StringLiteral(
        String stringValue    ) {
        super(
        );
        this.stringValue = stringValue;
    }


    public String getStringvalue() {
        return stringValue;
    }

    public void setStringvalue(String stringValue) {
        this.stringValue = stringValue;
    }


}
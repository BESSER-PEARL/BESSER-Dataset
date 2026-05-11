





import java.util.List;
import java.util.ArrayList;

public class notation_StringValueStyle extends NamedStyle {

    private String stringValue;



    public notation_StringValueStyle(
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
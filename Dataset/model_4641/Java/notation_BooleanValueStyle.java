





import java.util.List;
import java.util.ArrayList;

public class notation_BooleanValueStyle extends NamedStyle {

    private boolean booleanValue;



    public notation_BooleanValueStyle(
        boolean booleanValue    ) {
        super(
        );
        this.booleanValue = booleanValue;
    }


    public boolean getBooleanvalue() {
        return booleanValue;
    }

    public void setBooleanvalue(boolean booleanValue) {
        this.booleanValue = booleanValue;
    }


}
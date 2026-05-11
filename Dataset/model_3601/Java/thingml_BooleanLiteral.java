





import java.util.List;
import java.util.ArrayList;

public class thingml_BooleanLiteral extends Literal {

    private boolean boolValue;



    public thingml_BooleanLiteral(
        boolean boolValue    ) {
        super(
        );
        this.boolValue = boolValue;
    }


    public boolean getBoolvalue() {
        return boolValue;
    }

    public void setBoolvalue(boolean boolValue) {
        this.boolValue = boolValue;
    }


}
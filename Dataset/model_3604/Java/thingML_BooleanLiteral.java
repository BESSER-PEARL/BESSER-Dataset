





import java.util.List;
import java.util.ArrayList;

public class thingML_BooleanLiteral extends Literal {

    private boolean boolValue;



    public thingML_BooleanLiteral(
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
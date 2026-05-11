





import java.util.List;
import java.util.ArrayList;

public class thingML_BooleanLiteral extends Expression {

    private String boolValue;



    public thingML_BooleanLiteral(
        String boolValue    ) {
        super(
        );
        this.boolValue = boolValue;
    }


    public String getBoolvalue() {
        return boolValue;
    }

    public void setBoolvalue(String boolValue) {
        this.boolValue = boolValue;
    }


}
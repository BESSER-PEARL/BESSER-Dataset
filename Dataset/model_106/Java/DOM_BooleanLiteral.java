





import java.util.List;
import java.util.ArrayList;

public class DOM_BooleanLiteral extends Expression {

    private String booleanValue;



    public DOM_BooleanLiteral(
        String booleanValue    ) {
        super(
        );
        this.booleanValue = booleanValue;
    }


    public String getBooleanvalue() {
        return booleanValue;
    }

    public void setBooleanvalue(String booleanValue) {
        this.booleanValue = booleanValue;
    }


}
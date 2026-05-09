





import java.util.List;
import java.util.ArrayList;

public class JDTAST_BooleanLiteral extends Expression {

    private String booleanValue;



    public JDTAST_BooleanLiteral(
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
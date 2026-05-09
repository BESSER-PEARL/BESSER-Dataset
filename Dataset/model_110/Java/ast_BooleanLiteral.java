





import java.util.List;
import java.util.ArrayList;

public class ast_BooleanLiteral extends Expression {

    private boolean booleanValue;



    public ast_BooleanLiteral(
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
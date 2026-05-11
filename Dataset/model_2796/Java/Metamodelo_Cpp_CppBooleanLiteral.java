





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppBooleanLiteral extends CppExpression {

    private boolean booleanValue;



    public Metamodelo_Cpp_CppBooleanLiteral(
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
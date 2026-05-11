





import java.util.List;
import java.util.ArrayList;

public class logoASM_Constant extends Expression {

    private int integerValue;



    public logoASM_Constant(
        int integerValue    ) {
        super(
        );
        this.integerValue = integerValue;
    }


    public int getIntegervalue() {
        return integerValue;
    }

    public void setIntegervalue(int integerValue) {
        this.integerValue = integerValue;
    }


}
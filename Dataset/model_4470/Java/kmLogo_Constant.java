





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Constant extends Expression {

    private int integerValue;



    public kmLogo_Constant(
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
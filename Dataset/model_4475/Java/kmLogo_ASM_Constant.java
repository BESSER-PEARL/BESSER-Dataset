





import java.util.List;
import java.util.ArrayList;

public class kmLogo_ASM_Constant extends Expression {

    private String integerValue;



    public kmLogo_ASM_Constant(
        String integerValue    ) {
        super(
        );
        this.integerValue = integerValue;
    }


    public String getIntegervalue() {
        return integerValue;
    }

    public void setIntegervalue(String integerValue) {
        this.integerValue = integerValue;
    }


}
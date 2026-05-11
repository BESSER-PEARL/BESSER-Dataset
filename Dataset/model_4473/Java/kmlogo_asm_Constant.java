





import java.util.List;
import java.util.ArrayList;

public class kmlogo_asm_Constant extends Expression {

    private String integerValue;



    public kmlogo_asm_Constant(
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
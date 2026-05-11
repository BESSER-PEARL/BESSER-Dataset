





import java.util.List;
import java.util.ArrayList;

public class smc_DateLiteral extends Expression {

    private String value;



    public smc_DateLiteral(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}
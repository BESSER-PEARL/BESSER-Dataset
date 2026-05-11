





import java.util.List;
import java.util.ArrayList;

public class smc_IntLiteral extends Expression {

    private int value;



    public smc_IntLiteral(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}
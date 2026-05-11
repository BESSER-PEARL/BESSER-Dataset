





import java.util.List;
import java.util.ArrayList;

public class imp_IntConst extends Expr {

    private int value;



    public imp_IntConst(
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
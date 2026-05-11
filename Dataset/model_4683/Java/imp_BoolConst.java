





import java.util.List;
import java.util.ArrayList;

public class imp_BoolConst extends Expr {

    private boolean value;



    public imp_BoolConst(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}
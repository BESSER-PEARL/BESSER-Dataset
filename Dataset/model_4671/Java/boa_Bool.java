





import java.util.List;
import java.util.ArrayList;

public class boa_Bool extends Expr {

    private boolean value;



    public boa_Bool(
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






import java.util.List;
import java.util.ArrayList;

public class boa_Int extends Expr {

    private int value;



    public boa_Int(
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
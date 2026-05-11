





import java.util.List;
import java.util.ArrayList;

public class graph_IntConstant extends Expr {

    private int value;



    public graph_IntConstant(
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
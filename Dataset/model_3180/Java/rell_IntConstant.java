





import java.util.List;
import java.util.ArrayList;

public class rell_IntConstant extends Expression {

    private int value;



    public rell_IntConstant(
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
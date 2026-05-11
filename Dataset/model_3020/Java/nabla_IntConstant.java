





import java.util.List;
import java.util.ArrayList;

public class nabla_IntConstant extends Expression {

    private int value;



    public nabla_IntConstant(
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
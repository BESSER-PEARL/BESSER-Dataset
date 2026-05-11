





import java.util.List;
import java.util.ArrayList;

public class xs_LiteralInt extends Literal {

    private int value;



    public xs_LiteralInt(
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






import java.util.List;
import java.util.ArrayList;

public class xs_LiteralBool extends Literal {

    private boolean value;



    public xs_LiteralBool(
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
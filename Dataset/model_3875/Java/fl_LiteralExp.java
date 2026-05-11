





import java.util.List;
import java.util.ArrayList;

public class fl_LiteralExp extends Exp {

    private int value;



    public fl_LiteralExp(
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
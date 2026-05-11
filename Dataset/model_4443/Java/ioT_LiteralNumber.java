





import java.util.List;
import java.util.ArrayList;

public class ioT_LiteralNumber extends Condition {

    private int value;



    public ioT_LiteralNumber(
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
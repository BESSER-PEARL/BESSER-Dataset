





import java.util.List;
import java.util.ArrayList;

public class expression_IntegerValue extends Term {

    private int value;



    public expression_IntegerValue(
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
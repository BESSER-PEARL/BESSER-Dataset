





import java.util.List;
import java.util.ArrayList;

public class classes_LiteralInteger extends LiteralSpecification {

    private int value;



    public classes_LiteralInteger(
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
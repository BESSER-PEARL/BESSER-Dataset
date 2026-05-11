





import java.util.List;
import java.util.ArrayList;

public class expressions_Quantity extends ComparisonOperand {

    private int value;



    public expressions_Quantity(
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
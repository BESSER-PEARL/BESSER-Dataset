





import java.util.List;
import java.util.ArrayList;

public class dbl_TestStatement extends Statement {

    private int value;



    public dbl_TestStatement(
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
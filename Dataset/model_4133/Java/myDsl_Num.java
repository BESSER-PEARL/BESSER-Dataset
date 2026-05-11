





import java.util.List;
import java.util.ArrayList;

public class myDsl_Num extends Expression {

    private int value;



    public myDsl_Num(
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
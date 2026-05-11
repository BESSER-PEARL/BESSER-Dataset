





import java.util.List;
import java.util.ArrayList;

public class paplj_Num extends Expr {

    private int value;



    public paplj_Num(
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






import java.util.List;
import java.util.ArrayList;

public class exp_Lit extends Exp {

    private int value;



    public exp_Lit(
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
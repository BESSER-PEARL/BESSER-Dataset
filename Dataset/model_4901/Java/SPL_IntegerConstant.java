





import java.util.List;
import java.util.ArrayList;

public class SPL_IntegerConstant extends Constant {

    private int value;



    public SPL_IntegerConstant(
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
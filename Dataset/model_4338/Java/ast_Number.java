





import java.util.List;
import java.util.ArrayList;

public class ast_Number extends Operand {

    private int value;



    public ast_Number(
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
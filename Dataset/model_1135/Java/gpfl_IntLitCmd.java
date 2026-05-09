





import java.util.List;
import java.util.ArrayList;

public class gpfl_IntLitCmd extends GExpression {

    private int value;



    public gpfl_IntLitCmd(
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
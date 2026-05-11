





import java.util.List;
import java.util.ArrayList;

public class robochart_IntegerExp extends Expression {

    private int value;



    public robochart_IntegerExp(
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
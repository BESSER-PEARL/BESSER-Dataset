





import java.util.List;
import java.util.ArrayList;

public class model_IntValue extends Value {

    private int value;



    public model_IntValue(
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






import java.util.List;
import java.util.ArrayList;

public class sparql_IntegerValue extends Value {

    private int value;



    public sparql_IntegerValue(
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
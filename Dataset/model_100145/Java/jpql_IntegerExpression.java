





import java.util.List;
import java.util.ArrayList;

public class jpql_IntegerExpression extends Value {

    private int value;



    public jpql_IntegerExpression(
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
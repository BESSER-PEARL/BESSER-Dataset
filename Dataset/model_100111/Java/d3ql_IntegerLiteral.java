





import java.util.List;
import java.util.ArrayList;

public class d3ql_IntegerLiteral extends Literal {

    private int value;



    public d3ql_IntegerLiteral(
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
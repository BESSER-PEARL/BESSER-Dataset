





import java.util.List;
import java.util.ArrayList;

public class minilang_Integer extends IntExpression {

    private int value;



    public minilang_Integer(
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
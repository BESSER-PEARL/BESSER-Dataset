





import java.util.List;
import java.util.ArrayList;

public class webGui_NumberLiteral extends Value {

    private int value;



    public webGui_NumberLiteral(
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
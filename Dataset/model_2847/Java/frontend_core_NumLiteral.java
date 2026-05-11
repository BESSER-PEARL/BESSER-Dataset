





import java.util.List;
import java.util.ArrayList;

public class frontend_core_NumLiteral extends Expression {

    private int value;



    public frontend_core_NumLiteral(
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
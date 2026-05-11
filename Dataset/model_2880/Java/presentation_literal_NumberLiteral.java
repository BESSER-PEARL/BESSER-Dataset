





import java.util.List;
import java.util.ArrayList;

public class presentation_literal_NumberLiteral extends NumericLiteral {

    private int value;



    public presentation_literal_NumberLiteral(
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
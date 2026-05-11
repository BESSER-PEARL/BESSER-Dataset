





import java.util.List;
import java.util.ArrayList;

public class expressions_HexLiteral extends Literal {

    private int value;



    public expressions_HexLiteral(
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
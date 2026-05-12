





import java.util.List;
import java.util.ArrayList;

public class stext_IntLiteral extends Literal {

    private int value;



    public stext_IntLiteral(
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






import java.util.List;
import java.util.ArrayList;

public class express_IntLiteral extends IndexTerminal {

    private int value;



    public express_IntLiteral(
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
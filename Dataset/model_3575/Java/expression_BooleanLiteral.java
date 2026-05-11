





import java.util.List;
import java.util.ArrayList;

public class expression_BooleanLiteral extends Literal {

    private boolean value;



    public expression_BooleanLiteral(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}
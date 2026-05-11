





import java.util.List;
import java.util.ArrayList;

public class minilang_Boolean extends BooleanExpression {

    private boolean value;



    public minilang_Boolean(
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
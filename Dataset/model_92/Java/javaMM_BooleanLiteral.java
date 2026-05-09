





import java.util.List;
import java.util.ArrayList;

public class javaMM_BooleanLiteral extends Expression {

    private boolean value;



    public javaMM_BooleanLiteral(
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
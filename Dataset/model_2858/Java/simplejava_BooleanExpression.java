





import java.util.List;
import java.util.ArrayList;

public class simplejava_BooleanExpression extends ConstantExpression {

    private boolean value;



    public simplejava_BooleanExpression(
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
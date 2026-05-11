





import java.util.List;
import java.util.ArrayList;

public class nabla_BoolConstant extends Expression {

    private boolean value;



    public nabla_BoolConstant(
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
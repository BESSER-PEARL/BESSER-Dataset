





import java.util.List;
import java.util.ArrayList;

public class oogen_OOLogicalLiteral extends OOLogicalExpression {

    private boolean value;



    public oogen_OOLogicalLiteral(
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
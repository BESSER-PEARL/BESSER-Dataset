





import java.util.List;
import java.util.ArrayList;

public class oogen_OOFloatLiteral extends OOArithmeticExpression {

    private float value;



    public oogen_OOFloatLiteral(
        float value    ) {
        super(
        );
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}
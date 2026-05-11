





import java.util.List;
import java.util.ArrayList;

public class gremlin_DoubleLiteral extends Expression {

    private float value;



    public gremlin_DoubleLiteral(
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
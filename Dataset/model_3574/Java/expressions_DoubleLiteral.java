





import java.util.List;
import java.util.ArrayList;

public class expressions_DoubleLiteral extends Expression {

    private float value;



    public expressions_DoubleLiteral(
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
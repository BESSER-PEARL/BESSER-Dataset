





import java.util.List;
import java.util.ArrayList;

public class odemcustom_DoubleLiteral extends Expression {

    private float value;



    public odemcustom_DoubleLiteral(
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
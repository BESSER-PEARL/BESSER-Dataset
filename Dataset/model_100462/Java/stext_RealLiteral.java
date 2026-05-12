





import java.util.List;
import java.util.ArrayList;

public class stext_RealLiteral extends Literal {

    private float value;



    public stext_RealLiteral(
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
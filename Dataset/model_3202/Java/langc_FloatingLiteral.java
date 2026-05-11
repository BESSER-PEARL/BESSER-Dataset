





import java.util.List;
import java.util.ArrayList;

public class langc_FloatingLiteral extends Literal {

    private float value;



    public langc_FloatingLiteral(
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
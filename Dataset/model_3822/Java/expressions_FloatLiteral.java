





import java.util.List;
import java.util.ArrayList;

public class expressions_FloatLiteral extends Literal {

    private float value;



    public expressions_FloatLiteral(
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
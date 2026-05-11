





import java.util.List;
import java.util.ArrayList;

public class C_Expressions_FloatLiteral extends Literal {

    private float value;



    public C_Expressions_FloatLiteral(
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






import java.util.List;
import java.util.ArrayList;

public class smc_DoubleLiteral extends Expression {

    private float value;



    public smc_DoubleLiteral(
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
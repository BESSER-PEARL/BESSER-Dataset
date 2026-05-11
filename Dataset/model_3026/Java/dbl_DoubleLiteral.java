





import java.util.List;
import java.util.ArrayList;

public class dbl_DoubleLiteral extends L1Expr {

    private float value;



    public dbl_DoubleLiteral(
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
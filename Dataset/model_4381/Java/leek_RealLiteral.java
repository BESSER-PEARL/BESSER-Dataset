





import java.util.List;
import java.util.ArrayList;

public class leek_RealLiteral extends Expression {

    private float value;



    public leek_RealLiteral(
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
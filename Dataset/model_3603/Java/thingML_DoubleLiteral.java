





import java.util.List;
import java.util.ArrayList;

public class thingML_DoubleLiteral extends Expression {

    private float doubleValue;



    public thingML_DoubleLiteral(
        float doubleValue    ) {
        super(
        );
        this.doubleValue = doubleValue;
    }


    public float getDoublevalue() {
        return doubleValue;
    }

    public void setDoublevalue(float doubleValue) {
        this.doubleValue = doubleValue;
    }


}
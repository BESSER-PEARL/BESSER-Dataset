





import java.util.List;
import java.util.ArrayList;

public class thingml_DoubleLiteral extends Literal {

    private float doubleValue;



    public thingml_DoubleLiteral(
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
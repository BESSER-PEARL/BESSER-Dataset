





import java.util.List;
import java.util.ArrayList;

public class thingML_IntegerLiteral extends Expression {

    private int intValue;



    public thingML_IntegerLiteral(
        int intValue    ) {
        super(
        );
        this.intValue = intValue;
    }


    public int getIntvalue() {
        return intValue;
    }

    public void setIntvalue(int intValue) {
        this.intValue = intValue;
    }


}
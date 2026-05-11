





import java.util.List;
import java.util.ArrayList;

public class thingml_IntegerLiteral extends Literal {

    private int intValue;



    public thingml_IntegerLiteral(
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
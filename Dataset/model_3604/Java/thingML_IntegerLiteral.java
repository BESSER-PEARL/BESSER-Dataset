





import java.util.List;
import java.util.ArrayList;

public class thingML_IntegerLiteral extends Literal {

    private String intValue;



    public thingML_IntegerLiteral(
        String intValue    ) {
        super(
        );
        this.intValue = intValue;
    }


    public String getIntvalue() {
        return intValue;
    }

    public void setIntvalue(String intValue) {
        this.intValue = intValue;
    }


}
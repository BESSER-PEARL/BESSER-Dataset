





import java.util.List;
import java.util.ArrayList;

public class vql_NumberValue extends LiteralValueReference {

    private boolean negative;



    public vql_NumberValue(
        boolean negative    ) {
        super(
        );
        this.negative = negative;
    }


    public boolean getNegative() {
        return negative;
    }

    public void setNegative(boolean negative) {
        this.negative = negative;
    }


}
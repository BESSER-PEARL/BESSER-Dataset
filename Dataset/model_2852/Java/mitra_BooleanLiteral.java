





import java.util.List;
import java.util.ArrayList;

public class mitra_BooleanLiteral extends Literal {

    private boolean booleanValue;



    public mitra_BooleanLiteral(
        boolean booleanValue    ) {
        super(
        );
        this.booleanValue = booleanValue;
    }


    public boolean getBooleanvalue() {
        return booleanValue;
    }

    public void setBooleanvalue(boolean booleanValue) {
        this.booleanValue = booleanValue;
    }


}
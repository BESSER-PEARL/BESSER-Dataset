





import java.util.List;
import java.util.ArrayList;

public class mpl_LiteralValue extends AtomicExpression {

    private int rawValue;



    public mpl_LiteralValue(
        int rawValue    ) {
        super(
        );
        this.rawValue = rawValue;
    }


    public int getRawvalue() {
        return rawValue;
    }

    public void setRawvalue(int rawValue) {
        this.rawValue = rawValue;
    }


}
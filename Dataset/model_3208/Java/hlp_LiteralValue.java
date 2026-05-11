





import java.util.List;
import java.util.ArrayList;

public class hlp_LiteralValue extends AtomicExpression {

    private String rawValue;



    public hlp_LiteralValue(
        String rawValue    ) {
        super(
        );
        this.rawValue = rawValue;
    }


    public String getRawvalue() {
        return rawValue;
    }

    public void setRawvalue(String rawValue) {
        this.rawValue = rawValue;
    }


}
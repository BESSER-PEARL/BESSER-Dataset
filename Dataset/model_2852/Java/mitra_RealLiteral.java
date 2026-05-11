





import java.util.List;
import java.util.ArrayList;

public class mitra_RealLiteral extends Literal {

    private String floatValue;



    public mitra_RealLiteral(
        String floatValue    ) {
        super(
        );
        this.floatValue = floatValue;
    }


    public String getFloatvalue() {
        return floatValue;
    }

    public void setFloatvalue(String floatValue) {
        this.floatValue = floatValue;
    }


}
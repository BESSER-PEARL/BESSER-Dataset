





import java.util.List;
import java.util.ArrayList;

public class mil_ConstantInteger extends Value {

    private int rawValue;



    public mil_ConstantInteger(
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
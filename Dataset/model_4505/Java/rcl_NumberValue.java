





import java.util.List;
import java.util.ArrayList;

public class rcl_NumberValue extends RoverValue {

    private int nValue;



    public rcl_NumberValue(
        int nValue    ) {
        super(
        );
        this.nValue = nValue;
    }


    public int getNvalue() {
        return nValue;
    }

    public void setNvalue(int nValue) {
        this.nValue = nValue;
    }


}
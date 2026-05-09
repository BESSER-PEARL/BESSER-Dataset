





import java.util.List;
import java.util.ArrayList;

public class mMDSL_OperatorEqual  {

    private String notequal;
    private String equal;



    public mMDSL_OperatorEqual(
        String notequal,        String equal    ) {
        this.notequal = notequal;
        this.equal = equal;
    }


    public String getNotequal() {
        return notequal;
    }

    public void setNotequal(String notequal) {
        this.notequal = notequal;
    }
    public String getEqual() {
        return equal;
    }

    public void setEqual(String equal) {
        this.equal = equal;
    }


}
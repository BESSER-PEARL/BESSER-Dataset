





import java.util.List;
import java.util.ArrayList;

public class afpText_AttributeValue extends triplet {

    private String Reserved0;
    private String AttVal;



    public afpText_AttributeValue(
        String Reserved0,        String AttVal    ) {
        super(
        );
        this.Reserved0 = Reserved0;
        this.AttVal = AttVal;
    }


    public String getReserved0() {
        return Reserved0;
    }

    public void setReserved0(String Reserved0) {
        this.Reserved0 = Reserved0;
    }
    public String getAttval() {
        return AttVal;
    }

    public void setAttval(String AttVal) {
        this.AttVal = AttVal;
    }


}
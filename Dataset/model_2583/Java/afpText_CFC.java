





import java.util.List;
import java.util.ArrayList;

public class afpText_CFC extends structuredField {

    private String CFIRGLen;
    private String Retired1;



    public afpText_CFC(
        String CFIRGLen,        String Retired1    ) {
        super(
        );
        this.CFIRGLen = CFIRGLen;
        this.Retired1 = Retired1;
    }


    public String getCfirglen() {
        return CFIRGLen;
    }

    public void setCfirglen(String CFIRGLen) {
        this.CFIRGLen = CFIRGLen;
    }
    public String getRetired1() {
        return Retired1;
    }

    public void setRetired1(String Retired1) {
        this.Retired1 = Retired1;
    }


}
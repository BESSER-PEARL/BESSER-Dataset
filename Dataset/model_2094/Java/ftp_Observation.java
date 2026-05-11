





import java.util.List;
import java.util.ArrayList;

public class ftp_Observation  {

    private int faultLimit;
    private String name;



    public ftp_Observation(
        int faultLimit,        String name    ) {
        this.faultLimit = faultLimit;
        this.name = name;
    }


    public int getFaultlimit() {
        return faultLimit;
    }

    public void setFaultlimit(int faultLimit) {
        this.faultLimit = faultLimit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}
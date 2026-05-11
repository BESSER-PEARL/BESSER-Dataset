





import java.util.List;
import java.util.ArrayList;

public class xDstmdata_subtype  {

    private String tID;
    private String tString;





    private xDstmdata_tCompound xdstmdata_tcompound;


    public xDstmdata_subtype(
        String tID,        String tString    ) {
        this.tID = tID;
        this.tString = tString;
    }


    public String getTid() {
        return tID;
    }

    public void setTid(String tID) {
        this.tID = tID;
    }
    public String getTstring() {
        return tString;
    }

    public void setTstring(String tString) {
        this.tString = tString;
    }

    public xDstmdata_tCompound getXdstmdata_tcompound() {
        return xdstmdata_tcompound;
    }

    public void setXdstmdata_tcompound(xDstmdata_tCompound xdstmdata_tcompound) {
        this.xdstmdata_tcompound = xdstmdata_tcompound;
    }

}
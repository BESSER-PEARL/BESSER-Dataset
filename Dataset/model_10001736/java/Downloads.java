





import java.util.List;
import java.util.ArrayList;

public class Downloads  {

    private int dID;
    private int sID;



    public Downloads(
        int dID,        int sID    ) {
        this.dID = dID;
        this.sID = sID;
    }


    public int getDid() {
        return dID;
    }

    public void setDid(int dID) {
        this.dID = dID;
    }
    public int getSid() {
        return sID;
    }

    public void setSid(int sID) {
        this.sID = sID;
    }


}
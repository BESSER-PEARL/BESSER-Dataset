





import java.util.List;
import java.util.ArrayList;

public class Favourites  {

    private int fID;
    private int sID;



    public Favourites(
        int fID,        int sID    ) {
        this.fID = fID;
        this.sID = sID;
    }


    public int getFid() {
        return fID;
    }

    public void setFid(int fID) {
        this.fID = fID;
    }
    public int getSid() {
        return sID;
    }

    public void setSid(int sID) {
        this.sID = sID;
    }


}
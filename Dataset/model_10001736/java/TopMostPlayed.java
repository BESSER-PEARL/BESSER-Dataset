





import java.util.List;
import java.util.ArrayList;

public class TopMostPlayed  {

    private int sID;
    private int mpID;



    public TopMostPlayed(
        int sID,        int mpID    ) {
        this.sID = sID;
        this.mpID = mpID;
    }


    public int getSid() {
        return sID;
    }

    public void setSid(int sID) {
        this.sID = sID;
    }
    public int getMpid() {
        return mpID;
    }

    public void setMpid(int mpID) {
        this.mpID = mpID;
    }


}
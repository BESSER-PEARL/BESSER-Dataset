





import java.util.List;
import java.util.ArrayList;

public class Recently_Played  {

    private int sID;
    private int rpID;



    public Recently_Played(
        int sID,        int rpID    ) {
        this.sID = sID;
        this.rpID = rpID;
    }


    public int getSid() {
        return sID;
    }

    public void setSid(int sID) {
        this.sID = sID;
    }
    public int getRpid() {
        return rpID;
    }

    public void setRpid(int rpID) {
        this.rpID = rpID;
    }


}
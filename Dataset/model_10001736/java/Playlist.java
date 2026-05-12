





import java.util.List;
import java.util.ArrayList;

public class Playlist  {

    private String pDate;
    private String pName;
    private int pID;



    public Playlist(
        String pDate,        String pName,        int pID    ) {
        this.pDate = pDate;
        this.pName = pName;
        this.pID = pID;
    }


    public String getPdate() {
        return pDate;
    }

    public void setPdate(String pDate) {
        this.pDate = pDate;
    }
    public String getPname() {
        return pName;
    }

    public void setPname(String pName) {
        this.pName = pName;
    }
    public int getPid() {
        return pID;
    }

    public void setPid(int pID) {
        this.pID = pID;
    }


}
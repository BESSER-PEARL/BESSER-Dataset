





import java.util.List;
import java.util.ArrayList;

public class afpText_UP3iFinishingOperation extends triplet {

    private String UP3iDat;
    private String Seqnum;



    public afpText_UP3iFinishingOperation(
        String UP3iDat,        String Seqnum    ) {
        super(
        );
        this.UP3iDat = UP3iDat;
        this.Seqnum = Seqnum;
    }


    public String getUp3idat() {
        return UP3iDat;
    }

    public void setUp3idat(String UP3iDat) {
        this.UP3iDat = UP3iDat;
    }
    public String getSeqnum() {
        return Seqnum;
    }

    public void setSeqnum(String Seqnum) {
        this.Seqnum = Seqnum;
    }


}
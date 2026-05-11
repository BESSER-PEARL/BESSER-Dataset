





import java.util.List;
import java.util.ArrayList;

public class afpText_AttributeQualifier extends triplet {

    private String LevNum;
    private String SeqNum;



    public afpText_AttributeQualifier(
        String LevNum,        String SeqNum    ) {
        super(
        );
        this.LevNum = LevNum;
        this.SeqNum = SeqNum;
    }


    public String getLevnum() {
        return LevNum;
    }

    public void setLevnum(String LevNum) {
        this.LevNum = LevNum;
    }
    public String getSeqnum() {
        return SeqNum;
    }

    public void setSeqnum(String SeqNum) {
        this.SeqNum = SeqNum;
    }


}
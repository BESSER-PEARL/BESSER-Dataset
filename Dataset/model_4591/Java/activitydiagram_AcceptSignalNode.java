





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_AcceptSignalNode extends ActivityNode {

    private String signalId;



    public activitydiagram_AcceptSignalNode(
        String signalId    ) {
        super(
        );
        this.signalId = signalId;
    }


    public String getSignalid() {
        return signalId;
    }

    public void setSignalid(String signalId) {
        this.signalId = signalId;
    }


}
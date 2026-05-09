





import java.util.List;
import java.util.ArrayList;

public class pDL2_WorkSequenceKindStart  {

    private String Started2Start;
    private String Started2Finish;





    private pDL2_DependanceStart pdl2_dependancestart;


    public pDL2_WorkSequenceKindStart(
        String Started2Start,        String Started2Finish    ) {
        this.Started2Start = Started2Start;
        this.Started2Finish = Started2Finish;
    }


    public String getStarted2start() {
        return Started2Start;
    }

    public void setStarted2start(String Started2Start) {
        this.Started2Start = Started2Start;
    }
    public String getStarted2finish() {
        return Started2Finish;
    }

    public void setStarted2finish(String Started2Finish) {
        this.Started2Finish = Started2Finish;
    }

    public pDL2_DependanceStart getPdl2_dependancestart() {
        return pdl2_dependancestart;
    }

    public void setPdl2_dependancestart(pDL2_DependanceStart pdl2_dependancestart) {
        this.pdl2_dependancestart = pdl2_dependancestart;
    }

}
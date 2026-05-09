





import java.util.List;
import java.util.ArrayList;

public class pDL2_WorkSequenceKindFinish  {

    private String Finished2Start;
    private String Finished2Finish;





    private pDL2_DependanceFinish pdl2_dependancefinish;


    public pDL2_WorkSequenceKindFinish(
        String Finished2Start,        String Finished2Finish    ) {
        this.Finished2Start = Finished2Start;
        this.Finished2Finish = Finished2Finish;
    }


    public String getFinished2start() {
        return Finished2Start;
    }

    public void setFinished2start(String Finished2Start) {
        this.Finished2Start = Finished2Start;
    }
    public String getFinished2finish() {
        return Finished2Finish;
    }

    public void setFinished2finish(String Finished2Finish) {
        this.Finished2Finish = Finished2Finish;
    }

    public pDL2_DependanceFinish getPdl2_dependancefinish() {
        return pdl2_dependancefinish;
    }

    public void setPdl2_dependancefinish(pDL2_DependanceFinish pdl2_dependancefinish) {
        this.pdl2_dependancefinish = pdl2_dependancefinish;
    }

}
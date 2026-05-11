





import java.util.List;
import java.util.ArrayList;

public class afpText_FinishingOperation extends triplet {

    private String FOpCnt;
    private String RefEdge;
    private String OpPos;
    private String AxOffst;
    private String FOpType;



    public afpText_FinishingOperation(
        String FOpCnt,        String RefEdge,        String OpPos,        String AxOffst,        String FOpType    ) {
        super(
        );
        this.FOpCnt = FOpCnt;
        this.RefEdge = RefEdge;
        this.OpPos = OpPos;
        this.AxOffst = AxOffst;
        this.FOpType = FOpType;
    }


    public String getFopcnt() {
        return FOpCnt;
    }

    public void setFopcnt(String FOpCnt) {
        this.FOpCnt = FOpCnt;
    }
    public String getRefedge() {
        return RefEdge;
    }

    public void setRefedge(String RefEdge) {
        this.RefEdge = RefEdge;
    }
    public String getOppos() {
        return OpPos;
    }

    public void setOppos(String OpPos) {
        this.OpPos = OpPos;
    }
    public String getAxoffst() {
        return AxOffst;
    }

    public void setAxoffst(String AxOffst) {
        this.AxOffst = AxOffst;
    }
    public String getFoptype() {
        return FOpType;
    }

    public void setFoptype(String FOpType) {
        this.FOpType = FOpType;
    }


}
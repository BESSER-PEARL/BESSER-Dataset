





import java.util.List;
import java.util.ArrayList;

public class siddhi_MathGtLtOperation extends MathOperation {

    private String lt;
    private String gt_eq;
    private String lt_eq;
    private String gt;





    private siddhi_MathOperation siddhi_mathoperation;


    public siddhi_MathGtLtOperation(
        String lt,        String gt_eq,        String lt_eq,        String gt    ) {
        super(
        );
        this.lt = lt;
        this.gt_eq = gt_eq;
        this.lt_eq = lt_eq;
        this.gt = gt;
    }


    public String getLt() {
        return lt;
    }

    public void setLt(String lt) {
        this.lt = lt;
    }
    public String getGt_eq() {
        return gt_eq;
    }

    public void setGt_eq(String gt_eq) {
        this.gt_eq = gt_eq;
    }
    public String getLt_eq() {
        return lt_eq;
    }

    public void setLt_eq(String lt_eq) {
        this.lt_eq = lt_eq;
    }
    public String getGt() {
        return gt;
    }

    public void setGt(String gt) {
        this.gt = gt;
    }

    public siddhi_MathOperation getSiddhi_mathoperation() {
        return siddhi_mathoperation;
    }

    public void setSiddhi_mathoperation(siddhi_MathOperation siddhi_mathoperation) {
        this.siddhi_mathoperation = siddhi_mathoperation;
    }

}
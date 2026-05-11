





import java.util.List;
import java.util.ArrayList;

public class siddhi_MathEqualOperation extends MathOperation {

    private String not_eq;
    private String eq;





    private siddhi_MathAddsubOperation siddhi_mathaddsuboperation;


    public siddhi_MathEqualOperation(
        String not_eq,        String eq    ) {
        super(
        );
        this.not_eq = not_eq;
        this.eq = eq;
    }


    public String getNot_eq() {
        return not_eq;
    }

    public void setNot_eq(String not_eq) {
        this.not_eq = not_eq;
    }
    public String getEq() {
        return eq;
    }

    public void setEq(String eq) {
        this.eq = eq;
    }

    public siddhi_MathAddsubOperation getSiddhi_mathaddsuboperation() {
        return siddhi_mathaddsuboperation;
    }

    public void setSiddhi_mathaddsuboperation(siddhi_MathAddsubOperation siddhi_mathaddsuboperation) {
        this.siddhi_mathaddsuboperation = siddhi_mathaddsuboperation;
    }

}
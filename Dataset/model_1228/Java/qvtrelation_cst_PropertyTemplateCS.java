





import java.util.List;
import java.util.ArrayList;

public class qvtrelation_cst_PropertyTemplateCS extends CSTNode {

    private boolean opposite;





    private OCLExpressionCS oclexpressioncs;


    public qvtrelation_cst_PropertyTemplateCS(
        boolean opposite    ) {
        super(
        );
        this.opposite = opposite;
    }


    public boolean getOpposite() {
        return opposite;
    }

    public void setOpposite(boolean opposite) {
        this.opposite = opposite;
    }

    public OCLExpressionCS getOclexpressioncs() {
        return oclexpressioncs;
    }

    public void setOclexpressioncs(OCLExpressionCS oclexpressioncs) {
        this.oclexpressioncs = oclexpressioncs;
    }

}
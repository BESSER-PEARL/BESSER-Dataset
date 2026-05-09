





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_LogExp extends ImperativeExpression, OperationCallExp {






    private OclExpression oclexpression;


    public ImperativeOCL_LogExp(
    ) {
        super(
        );
    }



    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}
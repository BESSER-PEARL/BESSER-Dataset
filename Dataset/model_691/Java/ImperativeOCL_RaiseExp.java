





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_RaiseExp extends ImperativeExpression {






    private Type type;




    private OclExpression oclexpression;


    public ImperativeOCL_RaiseExp(
    ) {
        super(
        );
    }



    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}
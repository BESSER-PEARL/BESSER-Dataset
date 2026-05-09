





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_RaiseExp extends ImperativeExpression {






    private OclExpression oclexpression;




    private Type type;


    public ImperativeOCL_RaiseExp(
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
    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}
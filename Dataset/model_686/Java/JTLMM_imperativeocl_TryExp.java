





import java.util.List;
import java.util.ArrayList;

public class JTLMM_imperativeocl_TryExp extends ImperativeExpression {






    private OclExpression oclexpression;




    private List<Type> types;




    private OclExpression oclexpression;


    public JTLMM_imperativeocl_TryExp(
    ) {
        super(
        );
        this.types = new ArrayList<>();
    }

    public JTLMM_imperativeocl_TryExp(
        ArrayList<Type> types    ) {
        this.types = types;
    }


    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}
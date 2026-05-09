





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_CatchExp extends ImperativeExpression {






    private List<OclExpression> oclexpressions;




    private List<Type> types;


    public ImperativeOCL_CatchExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
        this.types = new ArrayList<>();
    }

    public ImperativeOCL_CatchExp(
        ArrayList<OclExpression> oclexpressions,        ArrayList<Type> types    ) {
        this.oclexpressions = oclexpressions;
        this.types = types;
    }


    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}
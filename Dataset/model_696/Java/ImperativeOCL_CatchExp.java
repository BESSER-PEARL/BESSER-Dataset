





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_CatchExp extends ImperativeExpression {






    private List<Type> types;




    private List<OclExpression> oclexpressions;


    public ImperativeOCL_CatchExp(
    ) {
        super(
        );
        this.types = new ArrayList<>();
        this.oclexpressions = new ArrayList<>();
    }

    public ImperativeOCL_CatchExp(
        ArrayList<Type> types,        ArrayList<OclExpression> oclexpressions    ) {
        this.types = types;
        this.oclexpressions = oclexpressions;
    }


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}
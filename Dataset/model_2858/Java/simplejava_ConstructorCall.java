





import java.util.List;
import java.util.ArrayList;

public class simplejava_ConstructorCall extends GenericExpression {






    private simplejava_Type simplejava_type;




    private List<simplejava_ConstantExpression> simplejava_constantexpressions;


    public simplejava_ConstructorCall(
    ) {
        super(
        );
        this.simplejava_constantexpressions = new ArrayList<>();
    }

    public simplejava_ConstructorCall(
        ArrayList<simplejava_ConstantExpression> simplejava_constantexpressions    ) {
        this.simplejava_constantexpressions = simplejava_constantexpressions;
    }


    public simplejava_Type getSimplejava_type() {
        return simplejava_type;
    }

    public void setSimplejava_type(simplejava_Type simplejava_type) {
        this.simplejava_type = simplejava_type;
    }
    public List<simplejava_ConstantExpression> getSimplejava_constantexpressions() {
        return simplejava_constantexpressions;
    }

    public void addSimplejava_constantexpression(Simplejava_constantexpression simplejava_constantexpression) {
        this.simplejava_constantexpressions.add(simplejava_constantexpression);
    }

}
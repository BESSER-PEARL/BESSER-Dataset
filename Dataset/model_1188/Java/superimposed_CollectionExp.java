





import java.util.List;
import java.util.ArrayList;

public class superimposed_CollectionExp extends OclExpression {






    private List<superimposed_OclExpression> superimposed_oclexpressions;


    public superimposed_CollectionExp(
    ) {
        super(
        );
        this.superimposed_oclexpressions = new ArrayList<>();
    }

    public superimposed_CollectionExp(
        ArrayList<superimposed_OclExpression> superimposed_oclexpressions    ) {
        this.superimposed_oclexpressions = superimposed_oclexpressions;
    }


    public List<superimposed_OclExpression> getSuperimposed_oclexpressions() {
        return superimposed_oclexpressions;
    }

    public void addSuperimposed_oclexpression(Superimposed_oclexpression superimposed_oclexpression) {
        this.superimposed_oclexpressions.add(superimposed_oclexpression);
    }

}
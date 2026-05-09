





import java.util.List;
import java.util.ArrayList;

public class superimposed_OperationCallExp extends PropertyCallExp {

    private String name;





    private List<superimposed_OclExpression> superimposed_oclexpressions;


    public superimposed_OperationCallExp(
        String name    ) {
        super(
        );
        this.name = name;
        this.superimposed_oclexpressions = new ArrayList<>();
    }

    public superimposed_OperationCallExp(
        String name        ArrayList<superimposed_OclExpression> superimposed_oclexpressions    ) {
        this.name = name;
        this.superimposed_oclexpressions = superimposed_oclexpressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<superimposed_OclExpression> getSuperimposed_oclexpressions() {
        return superimposed_oclexpressions;
    }

    public void addSuperimposed_oclexpression(Superimposed_oclexpression superimposed_oclexpression) {
        this.superimposed_oclexpressions.add(superimposed_oclexpression);
    }

}
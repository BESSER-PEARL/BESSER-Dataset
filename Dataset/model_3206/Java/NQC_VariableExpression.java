





import java.util.List;
import java.util.ArrayList;

public class NQC_VariableExpression extends ValueExpression {






    private NQC_Variable nqc_variable;




    private NQC_AssignmentStatement nqc_assignmentstatement;


    public NQC_VariableExpression(
    ) {
        super(
        );
    }



    public NQC_Variable getNqc_variable() {
        return nqc_variable;
    }

    public void setNqc_variable(NQC_Variable nqc_variable) {
        this.nqc_variable = nqc_variable;
    }
    public NQC_AssignmentStatement getNqc_assignmentstatement() {
        return nqc_assignmentstatement;
    }

    public void setNqc_assignmentstatement(NQC_AssignmentStatement nqc_assignmentstatement) {
        this.nqc_assignmentstatement = nqc_assignmentstatement;
    }

}
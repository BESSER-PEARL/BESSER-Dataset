





import java.util.List;
import java.util.ArrayList;

public class alf_InvocationOrAssignementOrDeclarationStatement extends Statement {






    private alf_NameExpression alf_nameexpression;




    private alf_AssignmentCompletion alf_assignmentcompletion;


    public alf_InvocationOrAssignementOrDeclarationStatement(
    ) {
        super(
        );
    }



    public alf_NameExpression getAlf_nameexpression() {
        return alf_nameexpression;
    }

    public void setAlf_nameexpression(alf_NameExpression alf_nameexpression) {
        this.alf_nameexpression = alf_nameexpression;
    }
    public alf_AssignmentCompletion getAlf_assignmentcompletion() {
        return alf_assignmentcompletion;
    }

    public void setAlf_assignmentcompletion(alf_AssignmentCompletion alf_assignmentcompletion) {
        this.alf_assignmentcompletion = alf_assignmentcompletion;
    }

}






import java.util.List;
import java.util.ArrayList;

public class alf_AssignmentCompletion  {

    private String op;





    private alf_ThisInvocationStatement alf_thisinvocationstatement;




    private alf_InvocationOrAssignementOrDeclarationStatement alf_invocationorassignementordeclarationstatement;




    private alf_Test alf_test;




    private alf_VariableDeclarationCompletion alf_variabledeclarationcompletion;




    private alf_SequenceElement alf_sequenceelement;


    public alf_AssignmentCompletion(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public alf_ThisInvocationStatement getAlf_thisinvocationstatement() {
        return alf_thisinvocationstatement;
    }

    public void setAlf_thisinvocationstatement(alf_ThisInvocationStatement alf_thisinvocationstatement) {
        this.alf_thisinvocationstatement = alf_thisinvocationstatement;
    }
    public alf_InvocationOrAssignementOrDeclarationStatement getAlf_invocationorassignementordeclarationstatement() {
        return alf_invocationorassignementordeclarationstatement;
    }

    public void setAlf_invocationorassignementordeclarationstatement(alf_InvocationOrAssignementOrDeclarationStatement alf_invocationorassignementordeclarationstatement) {
        this.alf_invocationorassignementordeclarationstatement = alf_invocationorassignementordeclarationstatement;
    }
    public alf_Test getAlf_test() {
        return alf_test;
    }

    public void setAlf_test(alf_Test alf_test) {
        this.alf_test = alf_test;
    }
    public alf_VariableDeclarationCompletion getAlf_variabledeclarationcompletion() {
        return alf_variabledeclarationcompletion;
    }

    public void setAlf_variabledeclarationcompletion(alf_VariableDeclarationCompletion alf_variabledeclarationcompletion) {
        this.alf_variabledeclarationcompletion = alf_variabledeclarationcompletion;
    }
    public alf_SequenceElement getAlf_sequenceelement() {
        return alf_sequenceelement;
    }

    public void setAlf_sequenceelement(alf_SequenceElement alf_sequenceelement) {
        this.alf_sequenceelement = alf_sequenceelement;
    }

}






import java.util.List;
import java.util.ArrayList;

public class alf_VariableDeclarationCompletion  {

    private String variableName;
    private boolean multiplicityIndicator;





    private alf_AssignmentCompletion alf_assignmentcompletion;




    private alf_InvocationOrAssignementOrDeclarationStatement alf_invocationorassignementordeclarationstatement;


    public alf_VariableDeclarationCompletion(
        String variableName,        boolean multiplicityIndicator    ) {
        this.variableName = variableName;
        this.multiplicityIndicator = multiplicityIndicator;
    }


    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }
    public boolean getMultiplicityindicator() {
        return multiplicityIndicator;
    }

    public void setMultiplicityindicator(boolean multiplicityIndicator) {
        this.multiplicityIndicator = multiplicityIndicator;
    }

    public alf_AssignmentCompletion getAlf_assignmentcompletion() {
        return alf_assignmentcompletion;
    }

    public void setAlf_assignmentcompletion(alf_AssignmentCompletion alf_assignmentcompletion) {
        this.alf_assignmentcompletion = alf_assignmentcompletion;
    }
    public alf_InvocationOrAssignementOrDeclarationStatement getAlf_invocationorassignementordeclarationstatement() {
        return alf_invocationorassignementordeclarationstatement;
    }

    public void setAlf_invocationorassignementordeclarationstatement(alf_InvocationOrAssignementOrDeclarationStatement alf_invocationorassignementordeclarationstatement) {
        this.alf_invocationorassignementordeclarationstatement = alf_invocationorassignementordeclarationstatement;
    }

}
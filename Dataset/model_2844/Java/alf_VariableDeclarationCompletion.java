





import java.util.List;
import java.util.ArrayList;

public class alf_VariableDeclarationCompletion  {

    private boolean multiplicityIndicator;
    private String variableName;





    private alf_InvocationOrAssignementOrDeclarationStatement alf_invocationorassignementordeclarationstatement;


    public alf_VariableDeclarationCompletion(
        boolean multiplicityIndicator,        String variableName    ) {
        this.multiplicityIndicator = multiplicityIndicator;
        this.variableName = variableName;
    }


    public boolean getMultiplicityindicator() {
        return multiplicityIndicator;
    }

    public void setMultiplicityindicator(boolean multiplicityIndicator) {
        this.multiplicityIndicator = multiplicityIndicator;
    }
    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }

    public alf_InvocationOrAssignementOrDeclarationStatement getAlf_invocationorassignementordeclarationstatement() {
        return alf_invocationorassignementordeclarationstatement;
    }

    public void setAlf_invocationorassignementordeclarationstatement(alf_InvocationOrAssignementOrDeclarationStatement alf_invocationorassignementordeclarationstatement) {
        this.alf_invocationorassignementordeclarationstatement = alf_invocationorassignementordeclarationstatement;
    }

}
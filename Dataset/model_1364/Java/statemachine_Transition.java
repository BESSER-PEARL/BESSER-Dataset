





import java.util.List;
import java.util.ArrayList;

public class statemachine_Transition extends Declaration {

    private String guardLabel;
    private String label;
    private String guardExpression;
    private String actionLabel;
    private String actionStatement;
    private String targetLabel;
    private String sourceLabel;



    public statemachine_Transition(
        String guardLabel,        String label,        String guardExpression,        String actionLabel,        String actionStatement,        String targetLabel,        String sourceLabel    ) {
        super(
        );
        this.guardLabel = guardLabel;
        this.label = label;
        this.guardExpression = guardExpression;
        this.actionLabel = actionLabel;
        this.actionStatement = actionStatement;
        this.targetLabel = targetLabel;
        this.sourceLabel = sourceLabel;
    }


    public String getGuardlabel() {
        return guardLabel;
    }

    public void setGuardlabel(String guardLabel) {
        this.guardLabel = guardLabel;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getGuardexpression() {
        return guardExpression;
    }

    public void setGuardexpression(String guardExpression) {
        this.guardExpression = guardExpression;
    }
    public String getActionlabel() {
        return actionLabel;
    }

    public void setActionlabel(String actionLabel) {
        this.actionLabel = actionLabel;
    }
    public String getActionstatement() {
        return actionStatement;
    }

    public void setActionstatement(String actionStatement) {
        this.actionStatement = actionStatement;
    }
    public String getTargetlabel() {
        return targetLabel;
    }

    public void setTargetlabel(String targetLabel) {
        this.targetLabel = targetLabel;
    }
    public String getSourcelabel() {
        return sourceLabel;
    }

    public void setSourcelabel(String sourceLabel) {
        this.sourceLabel = sourceLabel;
    }


}